from playwright.sync_api import sync_playwright

URL = "https://www.dot.gov.in/documents/press-release"


def get_latest_articles():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL, wait_until="networkidle", timeout=60000)

        print("Title:", page.title())

        html = page.content()

        with open("dot.html", "w", encoding="utf-8") as f:
            f.write(html)

        page.screenshot(path="dot.png", full_page=True)

        browser.close()

    print("Done")

    return []
