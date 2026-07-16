from sources.ookla import get_latest_articles
from telegram_service import send_message
from article_store import load_articles, save_articles

articles = get_latest_articles()
sent_articles = load_articles()

print(f"Found {len(articles)} articles")

for article in articles:

    if article["link"] in sent_articles:
        print("Already Sent:", article["title"])
        continue

    message = f"""📡 Ookla Latest News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)

    sent_articles.append(article["link"])
    save_articles(sent_articles)

    print("New Article Sent")
