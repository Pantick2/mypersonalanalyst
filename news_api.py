import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

def get_latest_news(category="general", country="gb", limit=15):
    if not NEWS_API_KEY:
        print("⚠️ NEWS_API_KEY nu este setată")
        return []

    if category == "legal":
        url = f"https://newsapi.org/v2/everything?q=law+legal+contract+regulation&language=en&sortBy=publishedAt&pageSize={limit}&apiKey={NEWS_API_KEY}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"

    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return data.get("articles", []) if data.get("status") == "ok" else []
    except Exception as e:
        print("Eroare preluare știri:", e)
        return []
