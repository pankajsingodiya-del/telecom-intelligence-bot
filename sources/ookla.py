import feedparser

RSS_URL = "https://www.ookla.com/articles/rss.xml"

def get_latest_articles():
    feed = feedparser.parse(RSS_URL)

    print("Feed Status:", feed.status if hasattr(feed, "status") else "No Status")
    print("Feed Title:", feed.feed.get("title", "No Title"))
    print("Entries:", len(feed.entries))

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })

    return articles
