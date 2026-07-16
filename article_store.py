import json
import os

FILE = "data/sent_articles.json"


def load_articles():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_articles(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def is_sent(link):
    articles = load_articles()
    return link in articles


def mark_sent(link):
    articles = load_articles()

    if link not in articles:
        articles.append(link)
        save_articles(articles)
