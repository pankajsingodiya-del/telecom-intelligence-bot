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
