import os
import requests
from datetime import datetime, timedelta

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

# --------------------------
# 📦 ZONA DE MEMORARE TEMPORARĂ
# --------------------------
cache = {}
CACHE_DURATA = 60 * 60  # ← Cât timp păstrăm știrile (în secunde) → aici = 1 oră

def get_latest_news(category="general", country="gb", limit=12):
    global cache
    cheie_cache = f"{category}_{country}"

    # ✅ Dacă avem date proaspete, le returnăm direct, FĂRĂ să mai apelăm API-ul
    if cheie_cache in cache:
        date, data_actualizare = cache[cheie_cache]
        if datetime.now() - data_actualizare < timedelta(seconds=CACHE_DURATA):
            print(f"✅ Folosesc știrile salvate pentru: {category}")
            return date

    # ✅ Dacă nu sunt sau sunt vechi, luăm altele noi
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY nu este setată!")
        # Dacă cheia lipsește, returnăm CE AM SALVAT ÎNAINTE
        return cache.get(cheie_cache, ([], datetime.now()))[0]

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    try:
        if category.lower() == "legal":
            url = (
                "https://newsapi.org/v2/everything?"
                "q=law+legal+contract+regulation+court&"
                "language=en&sortBy=publishedAt&pageSize={}&apiKey={}"
            ).format(limit, NEWS_API_KEY)
        else:
            url = (
                "https://newsapi.org/v2/top-headlines?"
                "country={}&category={}&pageSize={}&apiKey={}"
            ).format(country, category, limit, NEWS_API_KEY)

        resp = requests.get(url, headers=headers, timeout=12)

        # ⛔ Dacă API-ul refuză, folosim vechile știri salvate
        if resp.status_code == 429 or resp.status_code >= 400:
            print(f"⚠️ API indisponibil temporar, folosesc știrile salvate pentru: {category}")
            return cache.get(cheie_cache, ([], datetime.now()))[0]

        data = resp.json()

        if data.get("status") == "ok":
            articole = data.get("articles", [])
            # Salvăm noile știri în memorie
            cache[cheie_cache] = (articole, datetime.now())
            print(f"✅ Știri noi preluate și salvate pentru: {category}")
            return articole
        else:
            print(f"⚠️ Răspuns invalid API, folosesc știrile salvate")
            return cache.get(cheie_cache, ([], datetime.now()))[0]

    except Exception as e:
        print(f"❌ Eroare conexiune: {str(e)} | Folosesc știrile salvate")
        return cache.get(cheie_cache, ([], datetime.now()))[0]
