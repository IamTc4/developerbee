
import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Viewports to test (Mobile)
        viewports = [
            {"width": 375, "height": 800, "name": "375"}, # Typical mobile
        ]

        # URLs and selectors/areas to focus on
        tasks = [
            {"file": "index.html", "name": "index_tools", "full_page": True},
            {"file": "services.html", "name": "services_layout", "full_page": True},
            {"file": "pricing.html", "name": "pricing_page", "full_page": True},
        ]

        base_url = "http://localhost:3000"

        for task in tasks:
            for vp in viewports:
                await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
                try:
                    url = f"{base_url}/{task['file']}"
                    print(f"Navigating to {url}...")
                    await page.goto(url, wait_until="networkidle")
                    await page.wait_for_timeout(1000) # Wait for render

                    output_path = f"verification/issue_{task['name']}_{vp['name']}.png"
                    os.makedirs("verification", exist_ok=True)
                    await page.screenshot(path=output_path, full_page=True)
                    print(f"Saved {output_path}")
                except Exception as e:
                    print(f"Error capturing {task['file']}: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(take_screenshots())
