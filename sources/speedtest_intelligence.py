from playwright.sync_api import sync_playwright

URL = "https://www.speedtest.net/insights/blog"


def get_latest_articles():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )

        page.goto(URL, wait_until="networkidle", timeout=60000)

        print("Title:", page.title())
        print("Current URL:", page.url)

        html = page.content()

        with open("speedtest.html", "w", encoding="utf-8") as f:
            f.write(html)

        page.screenshot(path="speedtest.png", full_page=True)

        browser.close()

    print("Speedtest Intelligence Page Downloaded")

    return []
