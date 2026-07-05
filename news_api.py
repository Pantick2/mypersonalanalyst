# ✅ Am adăugat importul lipsă
import os
import requests
from dotenv import load_dotenv

# Încarcă cheia API din mediu
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

def get_latest_news(category="general", country="gb", limit=15):
    """
    Preia știri de la NewsAPI.org
    """
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY lipsește sau este goală")
        return []

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    # Categoria Legal → căutare globală
    if category.lower() == "legal":
        url = (
            "https://newsapi.org/v2/everything?"
            "q=law+legal+contract+regulation+court+business+dispute&"
            "language=en&sortBy=publishedAt&pageSize={}&apiKey={}"
        ).format(limit, NEWS_API_KEY)

    else:
        # Alte categorii → întâi pe țară
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country={}&category={}&pageSize={}&apiKey={}"
        ).format(country, category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        # Dacă nu sunt rezultate pe țară → încearcă global
        if data.get("status") == "ok" and len(data.get("articles", [])) == 0 and category != "legal":
            print(f"ℹ️ Fără știri pe {country} pentru {category} → încerc global")
            url = (
                "https://newsapi.org/v2/top-headlines?"
                "category={}&language=en&pageSize={}&apiKey={}"
            ).format(category, limit, NEWS_API_KEY)
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            data = resp.json()

        if data.get("status") == "ok":
            return data.get("articles", [])
        else:
            print(f"⚠️ NewsAPI răspuns: {data.get('message', 'necunoscut')}")
            return []

    except Exception as e:
        print(f"❌ Eroare NewsAPI: {str(e)}")
        return []
