from sources.ookla import get_latest_articles
from telegram_service import send_message

articles = get_latest_articles()

print(f"Found {len(articles)} articles")

if len(articles) == 0:
    send_message("❌ No Ookla news found.")
else:
    article = articles[0]

    message = f"""📡 Ookla Latest News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    print(message)
    send_message(message)
