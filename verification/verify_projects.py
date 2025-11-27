from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the portfolio page
        page.goto("http://localhost:8000/portfolio.html")

        # Check for the new section
        expect(page.get_by_text("More Projects")).to_be_visible()

        # Check for some of the new buttons
        expect(page.get_by_role("link", name="Business Website for a Real Estate Agent")).to_be_visible()
        expect(page.get_by_role("link", name="Fashion Brand Instagram Growth")).to_be_visible()
        expect(page.get_by_role("link", name="Sales Dashboard")).to_be_visible()

        # Take a screenshot of the new section
        # Scroll to the bottom to see the new section
        page.locator(".project-list-container").scroll_into_view_if_needed()
        page.screenshot(path="verification/projects_verification.png")

        browser.close()

if __name__ == "__main__":
    os.makedirs("verification", exist_ok=True)
    run()
