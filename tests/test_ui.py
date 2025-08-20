from playwright.sync_api import sync_playwright

def test_baidu_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.baidu.com")

        page.wait_for_selector("input#kw")
        page.fill("input#kw", "GitHub Actions")
        page.press("input#kw", "Enter")

        page.wait_for_selector("text=GitHub")
        assert "github" in page.content().lower()
        browser.close()
