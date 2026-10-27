#!/usr/bin/env python3
"""
render_graphic.py — Low-memory, pixel-perfect HTML/SVG to PNG renderer using Playwright.
Optimized for constrained 1GB RAM VPS environments while guaranteeing crisp webfont loading.

Usage:
  python3 render_graphic.py <input.html> <output.png> [width] [height] [--preview] [--no-audit]

After rendering, an automatic layout audit prints AUDIT warnings for:
  - visible text smaller than 18px (mobile legibility floor)
  - text crossing the 72px safe margin or clipped outside the canvas
  - bullet/dot glyphs (\u2022 \u25cf) that the skill bans
"""

import asyncio
import os
import sys
import time
from playwright.async_api import async_playwright

LOW_RAM_CHROMIUM_ARGS = [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-background-networking",
    "--disable-sync",
    "--disable-translate",
    "--no-first-run",
    "--no-zygote",
    "--single-process",
    "--js-flags=--max-old-space-size=64",
]

AUDIT_JS = """
({w, h, margin}) => {
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let n;
  while ((n = walker.nextNode())) {
    const txt = n.textContent.trim();
    if (!txt) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) continue;
    const range = document.createRange();
    range.selectNodeContents(n);
    const r = range.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const label = txt.slice(0, 40).replace(/\\s+/g, ' ');
    const fs = parseFloat(cs.fontSize);
    if (fs < 18) out.push(`font ${fs}px < 18px: "${label}"`);
    if (/[\u2022\u25cf\u25cb\u2219]/.test(txt)) out.push(`banned bullet/dot glyph: "${label}"`);
    if (r.left < 0 || r.top < 0 || r.right > w || r.bottom > h)
      out.push(`text clipped outside canvas: "${label}"`);
    else if (r.left < margin - 1 || r.right > w - margin + 1)
      out.push(`text inside ${margin}px side safe margin (x ${Math.round(r.left)}-${Math.round(r.right)}): "${label}"`);
  }
  return out;
}
"""


async def render(
    input_path: str,
    output_path: str,
    width: int = 1080,
    height: int = 1350,
    make_preview: bool = False,
    run_audit: bool = True,
) -> None:
    abs_input = os.path.abspath(input_path)
    abs_output = os.path.abspath(output_path)
    if not os.path.exists(abs_input):
        raise FileNotFoundError(f"Input HTML/SVG not found: {abs_input}")

    os.makedirs(os.path.dirname(abs_output) or ".", exist_ok=True)
    file_url = f"file://{abs_input}"
    t0 = time.time()
    issues: list = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=LOW_RAM_CHROMIUM_ARGS,
        )
        try:
            context = await browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1.0,
            )
            page = await context.new_page()
            try:
                await page.goto(file_url, wait_until="networkidle", timeout=25000)
            except Exception:
                # Fallback if external Google Fonts CDN is slow; still render cleanly
                await page.goto(file_url, wait_until="load", timeout=15000)

            # Wait explicitly for webfont faces to finish rasterizing
            try:
                await page.evaluate("() => document.fonts ? document.fonts.ready : Promise.resolve()")
            except Exception:
                pass
            # Wait for every <img> (local or remote) to finish decoding
            try:
                await page.evaluate(
                    """() => Promise.all([...document.images].map(i => i.complete ? 1 :
                        new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); })))"""
                )
            except Exception:
                pass
            await asyncio.sleep(0.5)

            if run_audit:
                try:
                    issues = await page.evaluate(AUDIT_JS, {"w": width, "h": height, "margin": 72})
                except Exception as exc:
                    issues = [f"audit skipped: {exc}"]

            await page.screenshot(
                path=abs_output,
                clip={"x": 0, "y": 0, "width": width, "height": height},
            )
        finally:
            await browser.close()

    if make_preview:
        from PIL import Image

        base, _ = os.path.splitext(abs_output)
        preview_path = f"{base}_preview.jpg"
        with Image.open(abs_output) as im:
            rgb = im.convert("RGB")
            rgb.thumbnail((max(1, width // 2), max(1, height // 2)), Image.Resampling.LANCZOS)
            rgb.save(preview_path, quality=88, optimize=True)
        print(f"Preview saved: {preview_path}")

    elapsed = time.time() - t0
    size_kb = os.path.getsize(abs_output) / 1024.0
    print(
        f"Rendered {abs_output} ({width}x{height}px, {size_kb:.1f} KB) in {elapsed:.2f}s"
    )
    if run_audit:
        if issues:
            for msg in issues[:25]:
                print(f"AUDIT: {msg}")
            print(f"AUDIT: {len(issues)} issue(s) found - fix them before delivering (SKILL.md Step 5).")
        else:
            print("AUDIT: clean (font floor, safe margins, no bullets).")


def main() -> None:
    flags = {"--preview", "--no-audit"}
    raw_args = [a for a in sys.argv[1:] if a not in flags]
    make_preview = "--preview" in sys.argv[1:]
    run_audit = "--no-audit" not in sys.argv[1:]

    if len(raw_args) < 2:
        print(
            "Usage: python3 render_graphic.py <input.html> <output.png> [width] [height] [--preview] [--no-audit]"
        )
        sys.exit(1)

    input_file = raw_args[0]
    output_file = raw_args[1]
    w = int(raw_args[2]) if len(raw_args) > 2 else 1080
    h = int(raw_args[3]) if len(raw_args) > 3 else 1350

    asyncio.run(render(input_file, output_file, w, h, make_preview=make_preview, run_audit=run_audit))


if __name__ == "__main__":
    main()
