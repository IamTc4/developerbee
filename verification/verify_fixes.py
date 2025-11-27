from playwright.sync_api import sync_playwright

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Emulate iPhone 12 to check mobile optimization and header
        device = p.devices['iPhone 12']
        context = browser.new_context(**device)
        page = context.new_page()

        # Check Geo Page
        print("Checking Geo Page...")
        page.goto("http://localhost:8000/geo/usa.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/geo_usa.png")
        print("Screenshot saved: verification/geo_usa.png")

        # Verify Header JS is working (menu should be toggleable)
        # Click hamburger
        page.click("#navToggle")
        # Wait a bit for transition
        page.wait_for_timeout(500)
        page.screenshot(path="verification/geo_usa_menu_open.png")
        print("Screenshot saved: verification/geo_usa_menu_open.png")

        # Check Services Page
        print("Checking Services Page...")
        page.goto("http://localhost:8000/services/web-app-development.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/services_webapp.png")

        # Click hamburger
        page.click("#navToggle")
        page.wait_for_timeout(500)
        page.screenshot(path="verification/services_webapp_menu_open.png")

        # Check Blogs Page
        print("Checking Blogs Page...")
        page.goto("http://localhost:8000/blogs/top-web-development-trends-in-2025.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/blogs_trends.png")

        # Click hamburger
        page.click("#navToggle")
        page.wait_for_timeout(500)
        page.screenshot(path="verification/blogs_trends_menu_open.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
