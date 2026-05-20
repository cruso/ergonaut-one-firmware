from pathlib import Path
from playwright.sync_api import sync_playwright

# Каталог с SVG файлами 
INPUT_DIR = Path("out")

svg_files = list(INPUT_DIR.rglob("*.svg"))

svg_path = Path("draw/out/all_layers.svg")

if not svg_files: 
    print("SVG files not found") 
    exit(1)

print(f"Found {len(svg_files)} SVG files")

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        viewport={
            "width": 3000,
            "height": 3000
        }
    )

    for svg_path in svg_files:
        print(f"Processing: {svg_path}")

        png_path = svg_path.with_suffix(".png")

        html = f"""
        <html>
        <body style="margin:0;background:white;">
        {svg_path.read_text(encoding='utf-8')}
        </body>
        </html>
        """

        page.set_content(html)

        svg = page.locator("svg")

        svg.screenshot(
            path=str(png_path),
            timeout=120000
        )

        print(f"Saved: {png_path}")

    browser.close()

print("DONE")