from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

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

    soup = BeautifulSoup(html, "html.parser")

    articles = []

    for a in soup.find_all("a", href=True):

        href = a["href"]
        title = a.get_text(" ", strip=True)

        if len(title) < 20:
            continue

        if "/articles/" not in href:
            continue

        if href.startswith("/"):
            href = "https://www.ookla.com" + href

        articles.append({
            "title": title,
            "link": href,
            "published": ""
        })

    # Remove duplicates
    unique = []
    seen = set()

    for article in articles:
        if article["link"] not in seen:
            unique.append(article)
            seen.add(article["link"])

    # Keep only latest 6 articles
    latest_articles = unique[:6]

    

    print("========== SPEEDTEST ARTICLES ==========")

    for article in latest_articles:
        print(article["title"])
        print(article["link"])
        print("--------------------------------")

    return latest_articles
