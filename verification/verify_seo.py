from playwright.sync_api import sync_playwright

def verify_seo_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Verify Home Page Title
        print("Verifying Home Page...")
        page.goto("http://localhost:8000/index.html")
        title = page.title()
        print(f"Home Title: {title}")
        expected_title = "Top Web Development & Digital Agency India | DeveloperBee"
        assert title == expected_title, f"Expected '{expected_title}', got '{title}'"
        page.screenshot(path="verification/home_seo.png")

        # 2. Verify a Blog Post
        print("Verifying Blog Post...")
        page.goto("http://localhost:8000/blogs/ai-driven-web-development.html")
        blog_h1 = page.locator("h1").inner_text()
        print(f"Blog H1: {blog_h1}")
        assert "AI-Driven Web Development" in blog_h1
        page.screenshot(path="verification/blog_seo.png")

        # 3. Verify a Project Page
        print("Verifying Project Page...")
        page.goto("http://localhost:8000/projects/fintech-dashboard-revamp.html")
        proj_h1 = page.locator("h1").inner_text()
        print(f"Project H1: {proj_h1}")
        assert "FinTech Dashboard Revamp" in proj_h1
        page.screenshot(path="verification/project_seo.png")

        browser.close()

if __name__ == "__main__":
    verify_seo_changes()
