#!/usr/bin/env python3
"""
render_graphic.py — Low-memory, pixel-perfect HTML/SVG to PNG renderer using Playwright.
Optimized for constrained 1GB RAM VPS environments while guaranteeing crisp webfont loading.

Usage:
  python3 render_graphic.py <input.html> <output.png> [width] [height] [--preview]
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


async def render(
    input_path: str,
    output_path: str,
    width: int = 1080,
    height: int = 1350,
    make_preview: bool = False,
) -> None:
    abs_input = os.path.abspath(input_path)
    abs_output = os.path.abspath(output_path)
    if not os.path.exists(abs_input):
        raise FileNotFoundError(f"Input HTML/SVG not found: {abs_input}")

    os.makedirs(os.path.dirname(abs_output) or ".", exist_ok=True)
    file_url = f"file://{abs_input}"
    t0 = time.time()

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
            await asyncio.sleep(0.5)

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


def main() -> None:
    raw_args = [a for a in sys.argv[1:] if a != "--preview"]
    make_preview = "--preview" in sys.argv[1:]

    if len(raw_args) < 2:
        print(
            "Usage: python3 render_graphic.py <input.html> <output.png> [width] [height] [--preview]"
        )
        sys.exit(1)

    input_file = raw_args[0]
    output_file = raw_args[1]
    w = int(raw_args[2]) if len(raw_args) > 2 else 1080
    h = int(raw_args[3]) if len(raw_args) > 3 else 1350

    asyncio.run(render(input_file, output_file, w, h, make_preview=make_preview))


if __name__ == "__main__":
    main()
