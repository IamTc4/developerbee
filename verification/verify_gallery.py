
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8000/projects/project-mobile-app-design.html')
        # Scroll down to the gallery section
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await page.wait_for_timeout(1000) # wait for any lazy loading images
        gallery_element = await page.query_selector('.gallery')
        if gallery_element:
            await gallery_element.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/gallery.png')
        else:
            print("Gallery element not found")
        await browser.close()

asyncio.run(main())
