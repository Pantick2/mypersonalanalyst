import os
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

def get_latest_news(category="general", country="gb", limit=12):
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY nu este setată!")
        return []

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    # Caz special pentru Legal - rămâne căutare globală
    if category.lower() == "legal":
        url = (
            "https://newsapi.org/v2/everything?"
            "q=law+legal+contract+regulation+court&"
            "language=en&sortBy=publishedAt&pageSize={}&apiKey={}"
        ).format(limit, NEWS_API_KEY)
    else:
        # Întâi încearcă pe țară
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country={}&category={}&pageSize={}&apiKey={}"
        ).format(country, category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 429:
            print("⚠️ Limita de cereri atinsă")
            return []
        resp.raise_for_status()
        data = resp.json()

        # Dacă nu sunt rezultate pe țară → caută global
        if data.get("status") == "ok" and len(data.get("articles", [])) == 0 and category.lower() != "legal":
            print(f"ℹ️ Fără știri pe {country} la {category} → încerc global")
            url = (
                "https://newsapi.org/v2/top-headlines?"
                "category={}&language=en&pageSize={}&apiKey={}"
            ).format(category, limit, NEWS_API_KEY)
            resp = requests.get(url, headers=headers, timeout=12)
            data = resp.json()

        return data.get("articles", []) if data.get("status") == "ok" else []

    except Exception as e:
        print(f"❌ Eroare: {str(e)}")
        return []
