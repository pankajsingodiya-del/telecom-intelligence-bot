import requests
from bs4 import BeautifulSoup

URL = "https://www.opensignal.com/blog"

def get_latest_articles():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=20)

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    for a in soup.select("a[href*='/blog/']"):
        title = a.get_text(strip=True)

        href = a.get("href")

        if not title:
            continue

        if href.startswith("/"):
            href = "https://www.opensignal.com" + href

        articles.append({
            "title": title,
            "link": href,
            "published": ""
        })

    return articles
