import os
import requests
from datetime import datetime, timedelta

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

# Cache pentru a păstra știrile și a nu face cereri inutile
cache = {}
CACHE_DURATA = 2 * 60 * 60  # Păstrăm știrile 2 ore

def get_latest_news(category="general", country="gb", limit=12):
    global cache
    cheie_cache = f"{category}_{country}"

    # ✅ Folosim știrile salvate dacă sunt proaspete
    if cheie_cache in cache:
        articole, data_salvare = cache[cheie_cache]
        if datetime.now() - data_salvare < timedelta(seconds=CACHE_DURATA):
            print(f"✅ Folosesc date salvate pentru: {category}")
            return articole

    if not NEWS_API_KEY:
        print("⚠️ Cheie API lipsă, afișez ultimele știri salvate")
        return cache.get(cheie_cache, ([], datetime.now()))[0]

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0",
        "Accept": "application/json"
    }

    try:
        # 🔹 Caz special pentru Legal - rămâne căutare globală
        if category.lower() == "legal":
            url = "https://newsapi.org/v2/everything?q=law+legal+contract+regulation&language=en&pageSize={}&apiKey={}".format(limit, NEWS_API_KEY)
            resp = requests.get(url, headers=headers, timeout=12)

        # 🔹 Pentru celelalte categorii: ÎNTÂI pe țară, DUPĂ global
        else:
            # Pasul 1: Caută în Marea Britanie
            url = "https://newsapi.org/v2/top-headlines?country={}&category={}&pageSize={}&apiKey={}".format(country, category, limit, NEWS_API_KEY)
            resp = requests.get(url, headers=headers, timeout=12)

            # Dacă nu sunt rezultate pe țară → căutăm global
            if resp.status_code == 200:
                date = resp.json()
                if date.get("status") == "ok" and len(date.get("articles", [])) == 0:
                    print(f"ℹ️ Fără știri în {country} la {category} → caut global")
                    url = "https://newsapi.org/v2/top-headlines?category={}&language=en&pageSize={}&apiKey={}".format(category, limit, NEWS_API_KEY)
                    resp = requests.get(url, headers=headers, timeout=12)

        # Dacă API-ul nu merge, returnăm ultimele știri salvate
        if resp.status_code != 200:
            print(f"⚠️ API indisponibil ({resp.status_code}), afișez date salvate")
            return cache.get(cheie_cache, ([], datetime.now()))[0]

        date = resp.json()
        articole = date.get("articles", []) if date.get("status") == "ok" else []

        # Dacă tot nu avem articole, păstrăm cele vechi
        if not articole:
            print(f"⚠️ Fără știri noi pentru {category}, păstrez cele salvate")
            return cache.get(cheie_cache, ([], datetime.now()))[0]

        # Salvăm noile știri
        cache[cheie_cache] = (articole, datetime.now())
        print(f"✅ Știri noi salvate pentru {category}")
        return articole

    except Exception as e:
        print(f"❌ Eroare: {str(e)} | Folosesc date salvate")
        return cache.get(cheie_cache, ([], datetime.now()))[0]
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
