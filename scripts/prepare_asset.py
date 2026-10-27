#!/usr/bin/env python3
"""
prepare_asset.py — Memory-safe asset preparation & seamless studio canvas blending.
Prevents Linux OOM crashes on huge images (via libjpeg draft decoding) and eliminates
visible rectangular bounding-box seams when placing dark/solid studio renders onto canvases.

Subcommands:
  1. Full-bleed cover crop (safe even on 100MP JPEGs):
     python3 prepare_asset.py cover <input> <output.jpg> [--width 1080] [--height 1350] [--focus top|center|bottom]

  2. Seamless studio placement enforcing the Spatial Yield Rule (zero bounding-box seam):
     python3 prepare_asset.py place-seamless <input> <output.jpg> [--zone bottom|top|center] [--bg "#050609"]
         [--top Y] [--bottom Y] [--align center|left|right] [--anchor center|top|bottom]
         [--scale 0.86] [--glow 0.12 --glow-color "#f97316"] [--width 1080] [--height 1350]
     - Transparent PNG cutouts keep original colors (no vignette); opaque renders get bg-matched + feathered.
     - The asset is always FIT inside the zone (never cropped) and prints ASSET_BOX for gap math.
"""

import argparse
import os
import numpy as np
from PIL import Image

# Guard against catastrophic RAM spikes while allowing controlled draft decoding
Image.MAX_IMAGE_PIXELS = 150_000_000


def parse_hex_color(hex_str: str) -> tuple[int, int, int]:
    s = hex_str.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6:
        raise ValueError(f"Invalid hex color: {hex_str}")
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def open_memory_safe(path: str, target_max_dim: int = 2400) -> Image.Image:
    """Open an image using libjpeg draft mode so giant JPEGs decode at low RAM."""
    im = Image.open(path)
    try:
        im.draft("RGB", (target_max_dim, target_max_dim))
    except Exception:
        pass
    im.load()
    if max(im.size) > target_max_dim * 1.5:
        ratio = target_max_dim / float(max(im.size))
        im = im.resize(
            (max(1, int(im.width * ratio)), max(1, int(im.height * ratio))),
            Image.Resampling.BILINEAR,
        )
    return im


def cmd_cover(args: argparse.Namespace) -> None:
    im = open_memory_safe(args.input, target_max_dim=max(args.width, args.height) * 2)
    im = im.convert("RGB")

    scale = max(args.width / im.width, args.height / im.height)
    nw = max(args.width, int(round(im.width * scale)))
    nh = max(args.height, int(round(im.height * scale)))
    scaled = im.resize((nw, nh), Image.Resampling.LANCZOS)

    left = (nw - args.width) // 2
    slack_y = nh - args.height
    if args.focus == "top":
        # Preserve head/face headroom on portraits while trimming bottom
        top = int(slack_y * 0.08)
    elif args.focus == "bottom":
        top = int(slack_y * 0.92)
    else:
        top = slack_y // 2

    cropped = scaled.crop((left, top, left + args.width, top + args.height))
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    cropped.save(args.output, quality=93, optimize=True)
    print(f"Saved cover-cropped asset: {args.output} ({args.width}x{args.height}, focus={args.focus})")


def _alpha_bbox(alpha: np.ndarray, thresh: float = 0.02):
    ys, xs = np.where(alpha > thresh)
    if ys.size == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def cmd_place_seamless(args: argparse.Namespace) -> None:
    bg_rgb = parse_hex_color(args.bg)
    target_bg = np.array(bg_rgb, dtype=np.float32)
    raw = open_memory_safe(args.input, target_max_dim=1800).convert("RGBA")

    # Detect true transparent cutouts (PNG/WebP with real alpha) vs opaque studio renders
    raw_alpha = np.asarray(raw.getchannel("A"), dtype=np.float32) / 255.0
    has_alpha = float((raw_alpha < 0.5).mean()) > 0.01
    if has_alpha:
        # Trim invisible padding so sizing/placement uses the real subject silhouette
        bbox = _alpha_bbox(raw_alpha)
        if bbox:
            raw = raw.crop(bbox)

    # Resolve the vertical zone the asset is allowed to occupy (Spatial Yield Rule, SKILL.md 2.1)
    if args.zone == "bottom":
        zone_top = args.top if args.top is not None else 520
        zone_bottom = args.bottom if args.bottom is not None else args.height - 40
    elif args.zone == "top":
        zone_top = args.top if args.top is not None else 60
        zone_bottom = args.bottom if args.bottom is not None else 780
    else:  # center / custom
        zone_top = args.top if args.top is not None else 120
        zone_bottom = args.bottom if args.bottom is not None else args.height - 120
    zone_top = max(0, zone_top)
    zone_bottom = min(args.height, zone_bottom)
    zone_h = max(1, zone_bottom - zone_top)

    # Fit INSIDE the zone (never crop/amputate the subject - SKILL.md 2.5 Asset Integrity)
    max_w = args.width * args.scale
    fit = min(max_w / raw.width, zone_h / raw.height)
    target_w = max(1, int(round(raw.width * fit)))
    target_h = max(1, int(round(raw.height * fit)))
    asset = raw.resize((target_w, target_h), Image.Resampling.LANCZOS)

    arr = np.asarray(asset, dtype=np.float32)
    rgb = arr[:, :, :3].copy()
    orig_alpha = arr[:, :, 3] / 255.0

    if has_alpha:
        # Clean cutout: keep subject colors untouched, alpha already defines the silhouette.
        final_alpha = orig_alpha
    else:
        # Opaque studio render: match its backdrop tone to the canvas hex, then feather edges to zero.
        b = max(1, min(12, target_h // 10, target_w // 10))
        border_pixels = np.concatenate(
            [
                rgb[:b, :, :].reshape(-1, 3),
                rgb[-b:, :, :].reshape(-1, 3),
                rgb[:, :b, :].reshape(-1, 3),
                rgb[:, -b:, :].reshape(-1, 3),
            ],
            axis=0,
        )
        edge_bg = np.median(border_pixels, axis=0)
        diff_from_edge = np.linalg.norm(rgb - edge_bg, axis=2)
        bg_similarity = np.clip(1.0 - (diff_from_edge / 42.0), 0.0, 1.0) ** 1.5
        rgb = np.clip(rgb + (target_bg - edge_bg) * bg_similarity[:, :, None], 0.0, 255.0)

        # Super-ellipse feather mask reaching exactly 0.0 at all 4 edges (zero rectangular seam)
        yy = np.linspace(-1.0, 1.0, target_h, dtype=np.float32)[:, None]
        xx = np.linspace(-1.0, 1.0, target_w, dtype=np.float32)[None, :]
        dist = (np.abs(xx) ** 3.2 + np.abs(yy) ** 3.2) ** (1.0 / 3.2)
        t = np.clip((dist - 0.68) / (0.995 - 0.68), 0.0, 1.0)
        final_alpha = orig_alpha * (1.0 - (t * t * (3.0 - 2.0 * t)))

    canvas = np.empty((args.height, args.width, 3), dtype=np.float32)
    canvas[:, :] = target_bg

    if args.glow > 0:
        # Subtle ambient radial glow behind the subject (opacity-controlled, never a hard disc)
        glow_rgb = np.array(parse_hex_color(args.glow_color), dtype=np.float32)
        cy = zone_top + zone_h / 2.0
        cx = args.width / 2.0
        gy = np.arange(args.height, dtype=np.float32)[:, None]
        gx = np.arange(args.width, dtype=np.float32)[None, :]
        r = np.sqrt(((gx - cx) / (target_w * 0.75)) ** 2 + ((gy - cy) / (target_h * 0.65)) ** 2)
        g = np.clip(1.0 - r, 0.0, 1.0) ** 2 * args.glow
        canvas = canvas * (1.0 - g[:, :, None]) + glow_rgb * g[:, :, None]

    margin = args.margin
    if args.align == "left":
        x_off = margin
    elif args.align == "right":
        x_off = args.width - margin - target_w
    else:
        x_off = (args.width - target_w) // 2
    if args.anchor == "top":
        y_off = zone_top
    elif args.anchor == "bottom":
        y_off = zone_bottom - target_h
    else:
        y_off = zone_top + (zone_h - target_h) // 2

    src_x0 = max(0, -x_off)
    src_y0 = max(0, -y_off)
    dst_x0 = max(0, x_off)
    dst_y0 = max(0, y_off)
    copy_w = min(target_w - src_x0, args.width - dst_x0)
    copy_h = min(target_h - src_y0, args.height - dst_y0)

    if copy_w > 0 and copy_h > 0:
        sub_rgb = rgb[src_y0 : src_y0 + copy_h, src_x0 : src_x0 + copy_w]
        sub_a = final_alpha[src_y0 : src_y0 + copy_h, src_x0 : src_x0 + copy_w, None]
        dst_slice = canvas[dst_y0 : dst_y0 + copy_h, dst_x0 : dst_x0 + copy_w]
        canvas[dst_y0 : dst_y0 + copy_h, dst_x0 : dst_x0 + copy_w] = (
            sub_rgb * sub_a + dst_slice * (1.0 - sub_a)
        )

    out_im = Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8))
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    out_im.save(args.output, quality=93, optimize=True)
    mode = "alpha-cutout" if has_alpha else "opaque-feathered"
    print(
        f"Saved seamless studio canvas: {args.output} ({args.width}x{args.height}, zone={args.zone}, "
        f"bg={args.bg}, mode={mode})"
    )
    # Exact subject bounds so the HTML layer can enforce Gap A == Gap B (SKILL.md 2.6)
    print(f"ASSET_BOX x={x_off} y={y_off} w={target_w} h={target_h} top={y_off} bottom={y_off + target_h}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Memory-safe graphic asset preparation")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_cover = sub.add_parser("cover", help="Memory-safe full-bleed cover crop")
    p_cover.add_argument("input")
    p_cover.add_argument("output")
    p_cover.add_argument("--width", type=int, default=1080)
    p_cover.add_argument("--height", type=int, default=1350)
    p_cover.add_argument("--focus", choices=["top", "center", "bottom"], default="center")
    p_cover.set_defaults(func=cmd_cover)

    p_place = sub.add_parser(
        "place-seamless",
        help="Blend isolated dark/solid-bg asset seamlessly onto canvas enforcing Spatial Yield",
    )
    p_place.add_argument("input")
    p_place.add_argument("output")
    p_place.add_argument("--zone", choices=["bottom", "top", "center"], default="bottom")
    p_place.add_argument("--top", type=int, default=None, help="Override zone top Y (px)")
    p_place.add_argument("--bottom", type=int, default=None, help="Override zone bottom Y (px)")
    p_place.add_argument("--align", choices=["center", "left", "right"], default="center")
    p_place.add_argument("--anchor", choices=["center", "top", "bottom"], default="center",
                         help="Vertical anchor of the asset inside its zone")
    p_place.add_argument("--margin", type=int, default=80, help="Side margin for left/right align")
    p_place.add_argument("--glow", type=float, default=0.0, help="Ambient glow opacity 0-0.3 (e.g. 0.12)")
    p_place.add_argument("--glow-color", default="#f97316")
    p_place.add_argument("--bg", default="#050609")
    p_place.add_argument("--width", type=int, default=1080)
    p_place.add_argument("--height", type=int, default=1350)
    p_place.add_argument("--scale", type=float, default=0.86)
    p_place.set_defaults(func=cmd_place_seamless)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
