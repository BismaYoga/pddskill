#!/usr/bin/env python3
"""
render_graphic.py — Render HTML/SVG graphic canvases to pixel-perfect PNG using Playwright.
Supports custom viewports (default 1080x1350 for Instagram 4:5).
"""

import sys
import os
import time
import asyncio
from playwright.async_api import async_playwright

async def render(input_path: str, output_path: str, width: int = 1080, height: int = 1350):
    abs_input = os.path.abspath(input_path)
    abs_output = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(abs_output), exist_ok=True)

    file_url = f"file://{abs_input}"
    t0 = time.time()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        context = await browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1.0
        )
        page = await context.new_page()
        await page.goto(file_url, wait_until="networkidle")
        # Ensure custom webfonts are loaded
        await asyncio.sleep(1.0)
        await page.screenshot(path=abs_output)
        await browser.close()

    elapsed = time.time() - t0
    print(f"Successfully rendered {abs_output} ({width}x{height}px) in {elapsed:.2f}s")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 render_graphic.py <input.html> <output.png> [width] [height]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    w = int(sys.argv[3]) if len(sys.argv) > 3 else 1080
    h = int(sys.argv[4]) if len(sys.argv) > 4 else 1350

    asyncio.run(render(input_file, output_file, w, h))

if __name__ == "__main__":
    main()
