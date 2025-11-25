
from playwright.sync_api import Page, expect, sync_playwright

def verify_home_page(page: Page):

  # 1. Arrange: Go to the Google homepage.
  page.goto("http://localhost:3000")

  # 2. Assert: Confirm the navigation was successful.
  expect(page).to_have_title("DeveloperBee | Custom Web & App Development in India")

  # 3. Screenshot: Capture the final result for visual verification.
  page.screenshot(path="verification/home_page.png")

if __name__ == "__main__":
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
      verify_home_page(page)
    finally:
      browser.close()
