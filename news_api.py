import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

def get_latest_news(category="general", country="gb", limit=10):
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY lipsește")
        return []

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    # Evităm cererile duplicate: folosim un singur endpoint pe categorie
    if category.lower() == "legal":
        url = (
            "https://newsapi.org/v2/everything?"
            "q=law+legal+contract+regulation&"
            "language=en&sortBy=publishedAt&pageSize={}&apiKey={}"
        ).format(limit, NEWS_API_KEY)
    else:
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country={}&category={}&pageSize={}&apiKey={}"
        ).format(country, category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        # Tratăm explicit eroarea 429
        if resp.status_code == 429:
            print("⚠️ NewsAPI: Limita de cereri atinsă (429). Revino mai târziu.")
            return []
        resp.raise_for_status()
        data = resp.json()
        return data.get("articles", []) if data.get("status") == "ok" else []

    except Exception as e:
        print(f"❌ Eroare NewsAPI: {str(e)}")
        return []
