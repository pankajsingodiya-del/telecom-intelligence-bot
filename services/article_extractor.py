from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def extract_article(url):

    browser = None

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.goto(url, wait_until="networkidle", timeout=60000)

            # Debug Information
            print("\n========== ARTICLE DEBUG ==========")
            print("Page Title:", page.title())
            print("Current URL:", page.url)

            html = page.content()

        soup = BeautifulSoup(html, "html.parser")

        print("Found <article> tags :", len(soup.find_all("article")))
        print("Found .td-post-content :", len(soup.select(".td-post-content")))
        print("Found .entry-content :", len(soup.select(".entry-content")))
        print("===================================\n")

        # Remove unwanted tags
        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        # Common article containers
        selectors = [
            ".td-post-content",      # TelecomTalk
            "article",
            ".entry-content",
            ".post-content",
            ".article-content",
            ".single-post-content",
            ".content",
            "main"
        ]

        container = None

        for selector in selectors:

            container = soup.select_one(selector)

            if container:
                print(f"Using Selector: {selector}")
                break

        if container:
            paragraphs = container.find_all("p")
        else:
            print("No article container found. Using all <p> tags.")
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

    finally:

        if browser:
            browser.close()
