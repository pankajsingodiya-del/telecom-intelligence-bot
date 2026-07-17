from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://insights.opensignal.com/market-insights"


def get_latest_articles():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )

       page.goto(URL, wait_until="networkidle", timeout=60000)

try:
    page.get_by_role("button", name="Allow all").click(timeout=5000)
    print("Cookie banner accepted")
except:
    print("No cookie banner found")

page.wait_for_timeout(3000)

        page.screenshot(path="opensignal.png", full_page=True)

        print("Page Title:", page.title())
        print("Current URL:", page.url)

        html = page.content()

        with open("opensignal.html", "w", encoding="utf-8") as f:
            f.write(html)

        browser.close()

    soup = BeautifulSoup(html, "html.parser")

    print("===== ALL LINKS =====")

print("Total links:", len(soup.find_all("a", href=True)))

    for a in soup.find_all("a", href=True):

        href = a["href"]
        title = a.get_text(" ", strip=True)

        print(title)
        print(href)
        print("----------------------")

    return []
