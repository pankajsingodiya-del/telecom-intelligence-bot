from sources.ookla import get_latest_articles as get_ookla_articles
from sources.opensignal import get_latest_articles as get_opensignal_articles
from sources.trai import get_latest_articles as get_trai_articles
from sources.telecom_news import get_latest_articles as get_telecom_news_articles
from sources.speedtest_intelligence import get_latest_articles as get_speedtest_articles
from sources.opensignal_reports import get_latest_articles as get_opensignal_reports

from telegram_service import send_message
from article_store import load_articles, save_articles


sent_articles = load_articles()


def process_source(source_name, emoji, articles):

    print(f"Found {len(articles)} {source_name} articles")

    for article in articles:

        if article["link"] in sent_articles:
            print("Already Sent:", article["title"])
            continue

        message = f"""{emoji} {source_name}

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

        send_message(message)

        sent_articles.append(article["link"])
        save_articles(sent_articles)

        print(f"New {source_name} Article Sent")


# ==========================================
# RUN ALL SOURCES
# ==========================================

process_source(
    "Ookla Latest News",
    "⚡",
    get_ookla_articles()
)

process_source(
    "OpenSignal Latest News",
    "📡",
    get_opensignal_articles()
)

process_source(
    "TRAI Update",
    "🇮🇳",
    get_trai_articles()
)

process_source(
    "Telecom News",
    "🌎",
    get_telecom_news_articles()
)

process_source(
    "Speedtest Intelligence",
    "📈",
    get_speedtest_articles()
)

# Debug only (currently doesn't return articles)
get_opensignal_reports()

print("====================================")
print("Telecom Intelligence Bot Completed")
print("====================================")
