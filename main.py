import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

message = """
🚀 Telecom Intelligence Bot Started Successfully!

✅ GitHub Actions Connected
✅ Telegram Connected

Next Step:
📡 Ookla Monitoring
📡 OpenSignal Monitoring

Powered by Pankaj 🚀
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

print(response.text)
