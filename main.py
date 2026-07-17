from sources.ookla import get_latest_articles as get_ookla_articles
from sources.opensignal import get_latest_articles as get_opensignal_articles
from sources.trai import get_latest_articles as get_trai_articles
from sources.telecom_news import get_latest_articles as get_telecom_news_articles

from telegram_service import send_message
from article_store import load_articles, save_articles


# Load previously sent articles
sent_articles = load_articles()


# ==========================================
# OOKLA
# ==========================================
ookla_articles = get_ookla_articles()

print(f"Found {len(ookla_articles)} Ookla articles")

for article in ookla_articles:

    if article["link"] in sent_articles:
        print("Already Sent:", article["title"])
        continue

    message = f"""⚡ Ookla Latest News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)

    sent_articles.append(article["link"])
    save_articles(sent_articles)

    print("New Ookla Article Sent")


# ==========================================
# OPENSIGNAL
# ==========================================
opensignal_articles = get_opensignal_articles()

print(f"Found {len(opensignal_articles)} OpenSignal articles")

for article in opensignal_articles:

    if article["link"] in sent_articles:
        print("Already Sent:", article["title"])
        continue

    message = f"""📡 OpenSignal Latest News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)

    sent_articles.append(article["link"])
    save_articles(sent_articles)

    print("New OpenSignal Article Sent")


# ==========================================
# TRAI
# ==========================================
trai_articles = get_trai_articles()

print(f"Found {len(trai_articles)} TRAI articles")

for article in trai_articles:

    if article["link"] in sent_articles:
        print("Already Sent:", article["title"])
        continue

    message = f"""🇮🇳 TRAI Update

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)

    sent_articles.append(article["link"])
    save_articles(sent_articles)

    print("New TRAI Article Sent")


# ==========================================
# TELECOM NEWS
# ==========================================
telecom_news_articles = get_telecom_news_articles()

print(f"Found {len(telecom_news_articles)} Telecom News articles")

for article in telecom_news_articles:

    if article["link"] in sent_articles:
        print("Already Sent:", article["title"])
        continue

    message = f"""🌎 Telecom News

📰 {article['title']}

🔗 {article['link']}

📅 {article['published']}
"""

    send_message(message)

    sent_articles.append(article["link"])
    save_articles(sent_articles)

    print("New Telecom News Article Sent")


print("====================================")
print("Telecom Intelligence Bot Completed")
print("====================================")

from sources.opensignal_reports import get_latest_articles as get_opensignal_reports

get_opensignal_reports()
