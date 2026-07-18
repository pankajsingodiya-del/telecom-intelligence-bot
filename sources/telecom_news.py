import feedparser

RSS_URL = "https://telecomtalk.info/feed/"


def get_latest_articles():

    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries:

        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })

    

    return articles
