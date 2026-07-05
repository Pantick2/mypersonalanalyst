import os
from dotenv import load_dotenv
import requests

# Încarcă automat din .env
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

def get_latest_news(category="general", country="gb", limit=15):
    if not NEWS_API_KEY:
        print("⚠️ Cheia API nu este setată")
        return []

    if category == "legal":
        url = f"https://newsapi.org/v2/everything?q=law+legal+contract+regulation&language=en&apiKey={NEWS_API_KEY}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={NEWS_API_KEY}"

    try:
        res = requests.get(url, timeout=10)
        return res.json().get("articles", [])
    except Exception as e:
        print("Eroare:", e)
        return []
