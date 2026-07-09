import os
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

# Salvăm ultimele știri aici
stiri_salvate = {}

def get_latest_news(category="general", country="gb", limit=12):
    global stiri_salvate

    if not NEWS_API_KEY:
        # Dacă nu avem cheie, returnăm ultimele știri salvate
        return stiri_salvate.get(category, [])

    headers = {"User-Agent": "Mozilla/5.0"}

    if category.lower() == "legal":
        url = "https://newsapi.org/v2/everything?q=law+legal+contract&language=en&pageSize={}&apiKey={}".format(limit, NEWS_API_KEY)
    else:
        url = "https://newsapi.org/v2/top-headlines?category={}&language=en&pageSize={}&apiKey={}".format(category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            # Dacă API-ul nu merge, folosim ce avem salvat
            return stiri_salvate.get(category, [])

        data = resp.json()
        articole = data.get("articles", []) if data.get("status") == "ok" else []

        if not articole:
            # Dacă nu sunt articole noi, păstrăm cele vechi
            return stiri_salvate.get(category, [])

        # Salvăm noile știri
        stiri_salvate[category] = articole
        return articole

    except:
        # La orice eroare, folosim știrile salvate
        return stiri_salvate.get(category, [])
