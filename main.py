from sources.ookla import get_latest_articles
from telegram_service import send_message
from article_store import is_sent, mark_sent

articles = get_latest_articles()

print(f"Found {len(articles)} articles")

for article in articles:

    if is_sent(article["link"]):
        print("Already Sent:", article["title"])
        continue

    message = f"""📡 Ookla Latest News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)
    mark_sent(article["link"])

    print("New Article Sent")
