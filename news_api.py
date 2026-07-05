import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

def get_latest_news(category="general", country="gb", limit=12):
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY nu este setată în mediu!")
        return []

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    if category.lower() == "legal":
        url = (
            "https://newsapi.org/v2/everything?"
            "q=law+legal+contract+regulation+court+business+dispute&"
            "language=en&sortBy=publishedAt&pageSize={}&apiKey={}"
        ).format(limit, NEWS_API_KEY)
    else:
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country={}&category={}&pageSize={}&apiKey={}"
        ).format(country, category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 429:
            print("⚠️ Limita de cereri NewsAPI atinsă, reîncearcă mai târziu")
            return []
        resp.raise_for_status()
        data = resp.json()
        return data.get("articles", []) if data.get("status") == "ok" else []
    except Exception as e:
        print(f"❌ Eroare preluare știri: {str(e)}")
        return []
