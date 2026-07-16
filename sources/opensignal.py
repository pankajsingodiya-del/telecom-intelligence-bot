import requests
from bs4 import BeautifulSoup

URL = "https://insights.opensignal.com/market-insights"


def get_latest_articles():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=30)

    print("Status:", response.status_code)
    print("Final URL:", response.url)

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    # Debug
    print("Total Links:", len(soup.find_all("a")))

    for link in soup.find_all("a", href=True):

        href = link["href"]
        title = link.get_text(strip=True)

        if not title:
            continue

        if "/market-insights" not in href:
            continue

        if href.startswith("/"):
            href = "https://insights.opensignal.com" + href

        articles.append({
            "title": title,
            "link": href,
            "published": ""
        })

    # Remove duplicate links
    unique = []
    seen = set()

    for article in articles:
        if article["link"] not in seen:
            unique.append(article)
            seen.add(article["link"])

    print("Found", len(unique), "articles")

    return unique
