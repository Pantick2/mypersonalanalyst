import os
import requests
from datetime import datetime, timedelta

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

# 📦 Cache simplu în memorie + fallback la date vechi
cache = {}
CACHE_DURATA = 2 * 60 * 60  # 2 ore

def get_latest_news(category="general", country="gb", limit=12):
    global cache
    cheie = f"{category}_{country}"

    # Folosim datele salvate dacă sunt proaspete
    if cheie in cache:
        date, data = cache[cheie]
        if datetime.now() - data < timedelta(seconds=CACHE_DURATA):
            print(f"✅ Folosesc date salvate: {category}")
            return date

    # Dacă nu avem cheie, returnăm ultimele date salvate
    if not NEWS_API_KEY:
        print("⚠️ Cheie API lipsă, folosesc date salvate")
        return cache.get(cheie, ([], datetime.now()))[0]

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0",
        "Accept": "application/json"
    }

    try:
        # Construim URL corect
        if category.lower() == "legal":
            url = "https://newsapi.org/v2/everything?q=law+legal+contract&language=en&pageSize={}&apiKey={}".format(limit, NEWS_API_KEY)
        else:
            url = "https://newsapi.org/v2/top-headlines?country={}&category={}&pageSize={}&apiKey={}".format(country, category, limit, NEWS_API_KEY)

        resp = requests.get(url, headers=headers, timeout=12)

        # Dacă API-ul nu merge, returnăm datele vechi
        if resp.status_code != 200:
            print(f"⚠️ API indisponibil, folosesc date salvate")
            return cache.get(cheie, ([], datetime.now()))[0]

        data = resp.json()
        articole = data.get("articles", []) if data.get("status") == "ok" else []

        # Dacă nu avem articole noi, păstrăm cele vechi
        if not articole:
            print(f"⚠️ Fără date noi, păstrez cele salvate")
            return cache.get(cheie, ([], datetime.now()))[0]

        # Salvăm noile articole
        cache[cheie] = (articole, datetime.now())
        print(f"✅ Date noi preluate pentru {category}")
        return articole

    except Exception as e:
        print(f"❌ Eroare: {str(e)}")
        return cache.get(cheie, ([], datetime.now()))[0]
