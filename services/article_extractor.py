import requests
from bs4 import BeautifulSoup


def extract_article(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code != 200:
            return ""

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        article_text = ""

        for p in paragraphs:

            text = p.get_text(" ", strip=True)

            if len(text) > 30:
                article_text += text + "\n"

        return article_text

    except Exception as e:

        print("Article Extract Error:", e)

        return ""
