from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def extract_article(url):

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.goto(url, wait_until="networkidle", timeout=60000)

            html = page.content()

            browser.close()

        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted elements
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
            ".content",
            "main"
        ]

        container = None

        for selector in selectors:
            container = soup.select_one(selector)
            if container:
                break

        if container:
            paragraphs = container.find_all("p")
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
