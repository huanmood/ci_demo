from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.fill("input[name='q']", "GitHub Actions")
        page.press("input[name='q']", "Enter")
        assert "GitHub" in page.title()
        browser.close()
