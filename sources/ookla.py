import requests
from bs4 import BeautifulSoup

URL = "https://www.ookla.com/articles"


def get_latest_articles():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    if response.status_code != 200:
        print("Website Error:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("a", href=True)

    print("Total Cards:", len(cards))

    article_count = 0

    for card in cards:

        href = card.get("href", "")

        if "/articles/" in href and href != "/articles":

            print("=" * 80)
            print(card.prettify())

            article_count += 1

            if article_count == 2:
                break

    articles = []

    for card in cards:

        href = card.get("href", "")

        if "/articles/" in href and href != "/articles":

            title = card.get_text(" ", strip=True)

            if len(title) > 20:
                articles.append({
                    "title": title,
                    "link": "https://www.ookla.com" + href,
                    "published": ""
                })

    return articles[:5]
