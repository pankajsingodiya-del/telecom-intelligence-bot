from sources.opensignal import get_latest_articles

articles = get_latest_articles()

print(f"Found {len(articles)} articles")

for article in articles[:10]:
    print(article["title"])
    print(article["link"])
    print("-" * 60)
