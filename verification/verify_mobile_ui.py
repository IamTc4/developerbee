from playwright.sync_api import sync_playwright

def verify_mobile_ui():
    with sync_playwright() as p:
        # Use a mobile device emulator
        iphone_12 = p.devices['iPhone 12']
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**iphone_12)
        page = context.new_page()

        # Pricing Page Verification
        print("Navigating to Pricing Page...")
        page.goto("http://localhost:3000/pricing.html")
        page.wait_for_load_state('networkidle')

        # Check Pricing Card Width
        # We expect the card to be almost full width.
        # iPhone 12 width is 390px. 85vw is ~331px.
        card = page.locator('.pricing-card').first
        box = card.bounding_box()
        print(f"Pricing Card Width: {box['width']}")

        # Take screenshot of Pricing Page
        page.screenshot(path="verification/mobile_pricing.png", full_page=True)

        # Scroll down to trigger sticky header hide
        print("Scrolling down...")
        page.mouse.wheel(0, 500)
        page.wait_for_timeout(500) # Wait for animation

        # Check if header is hidden
        header = page.locator('#mainHeader')
        # We expect the class 'header-hidden'
        if "header-hidden" in header.get_attribute("class"):
             print("Header is hidden on scroll down.")
        else:
             print("Header NOT hidden on scroll down.")

        page.screenshot(path="verification/mobile_pricing_scrolled.png")

        # Scroll up to trigger sticky header show
        print("Scrolling up...")
        page.mouse.wheel(0, -200)
        page.wait_for_timeout(500)

        if "header-hidden" not in header.get_attribute("class"):
             print("Header is shown on scroll up.")
        else:
             print("Header NOT shown on scroll up.")

        page.screenshot(path="verification/mobile_pricing_scroll_up.png")

        # About Page Verification (Left Orientation)
        print("Navigating to About Page...")
        page.goto("http://localhost:3000/about.html")
        page.wait_for_load_state('networkidle')
        page.screenshot(path="verification/mobile_about.png", full_page=True)

        # Services Page Verification
        print("Navigating to Services Page...")
        page.goto("http://localhost:3000/services.html")
        page.wait_for_load_state('networkidle')
        page.screenshot(path="verification/mobile_services.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_mobile_ui()
