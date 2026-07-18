import requests
from bs4 import BeautifulSoup


def extract_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        # Try common article containers
        selectors = [
            "article",
            ".post-content",
            ".entry-content",
            ".td-post-content",
            ".article-content",
            ".single-post-content",
            ".content"
        ]

        article = None

        for selector in selectors:
            article = soup.select_one(selector)
            if article:
                break

        if article:
            paragraphs = article.find_all("p")
        else:
            paragraphs = soup.find_all("p")

        text = []

        for p in paragraphs:
            line = p.get_text(" ", strip=True)

            if len(line) > 40:
                text.append(line)

        return "\n\n".join(text)

    except Exception as e:
        print("Article Extract Error:", e)
        return ""
