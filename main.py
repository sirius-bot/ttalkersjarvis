
import os
from flask import Flask, request
import requests

app = Flask(__name__)

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def send_to_notion(text):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        }
    }
    requests.post(url, json=data, headers=headers)

@app.route(f"/bot", methods=["POST"])
def telegram_webhook():
    data = request.json
    if "message" in data and "text" in data["message"]:
        user_text = data["message"]["text"]
        send_to_notion(user_text)
    return "ok"

@app.route("/")
def home():
    return "Bot running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
