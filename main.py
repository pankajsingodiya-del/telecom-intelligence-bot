from sources.ookla import get_latest_articles

articles = get_latest_articles()

print("Total Articles:", len(articles))
print(articles)
