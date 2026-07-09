import os
import json
import requests
from datetime import datetime, timedelta

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

# Calea către fișierul cu știri salvate
CACHE_FISIER = "stiri_salvate.json"
CACHE_DURATA = 2 * 60 * 60  # 2 ore

def incarca_stiri_salvate():
    if os.path.exists(CACHE_FISIER):
        try:
            with open(CACHE_FISIER, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def salveaza_stiri_noi(date):
    try:
        with open(CACHE_FISIER, "w", encoding="utf-8") as f:
            json.dump(date, f, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Nu am putut salva știrile: {e}")

def get_latest_news(category="general", country="gb", limit=12):
    cache = incarca_stiri_salvate()
    cheie_cache = f"{category}_{country}"

    date_salvate = cache.get(cheie_cache, {})
    articole_vechi = date_salvate.get("articole", [])
    data_actualizare = datetime.fromisoformat(date_salvate.get("data", "2000-01-01T00:00:00"))

    if datetime.now() - data_actualizare < timedelta(seconds=CACHE_DURATA):
        print(f"✅ Folosesc știrile salvate pentru {category}")
        return articole_vechi

    if not NEWS_API_KEY:
        print("⚠️ Cheie API lipsă, afișez ultimele știri salvate")
        return articole_vechi

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    try:
        if category.lower() == "legal":
            url = "https://newsapi.org/v2/everything?q=law+legal+contract&language=en&pageSize={}&apiKey={}".format(limit, NEWS_API_KEY)
        else:
            url = "https://newsapi.org/v2/top-headlines?country={}&category={}&pageSize={}&apiKey={}".format(country, category, limit, NEWS_API_KEY)

        resp = requests.get(url, headers=headers, timeout=12)

        if resp.status_code != 200:
            print(f"⚠️ API indisponibil ({resp.status_code}), afișez știrile salvate")
            return articole_vechi

        data = resp.json()
        articole_noi = data.get("articles", []) if data.get("status") == "ok" else []

        if not articole_noi:
            print(f"⚠️ Fără știri noi pentru {category}, păstrez cele salvate")
            return articole_vechi

        cache[cheie_cache] = {
            "articole": articole_noi,
            "data": datetime.now().isoformat()
        }
        salveaza_stiri_noi(cache)
        print(f"✅ Știri noi salvate pentru {category}")
        return articole_noi

    except Exception as e:
        print(f"❌ Eroare: {str(e)} | Afișez știrile salvate")
        return articole_vechi
    cache = incarca_stiri_salvate()
    cheie_cache = f"{category}_{country}"

    # ✅ Întâi verificăm dacă avem date salvate, indiferent de vechime
    date_salvate = cache.get(cheie_cache, {})
    articole_vechi = date_salvate.get("articole", [])
    data_actualizare = datetime.fromisoformat(date_salvate.get("data", "2000-01-01T00:00:00"))

    # Dacă avem date proaspete, le returnăm direct
    if datetime.now() - data_actualizare < timedelta(seconds=CACHE_DURATA):
        print(f"✅ Folosesc știrile salvate pentru {category}")
        return articole_vechi

    # Dacă nu avem cheie API, returnăm ce avem salvat
    if not NEWS_API_KEY:
        print("⚠️ Cheie API lipsă, afișez ultimele știri salvate")
        return articole_vechi

    headers = {
        "User-Agent": "MyPersonalAnalyst/1.0 (+https://mypersonalanalyst.com)",
        "Accept": "application/json"
    }

    try:
        # Construim URL
        if category.lower() == "legal":
            url = f"https://newsapi.org/v2/everything?q=law+legal+contract&language=en&pageSize={limit}&apiKey={NEWS_API_KEY}"
        else:
            url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"

        resp = requests.get(url, headers=headers, timeout=12)

        # Dacă API-ul nu merge, returnăm automat știrile vechi
        if resp.status_code != 200:
            print(f"⚠️ API indisponibil ({resp.status_code}), afișez știrile salvate")
            return articole_vechi

        data = resp.json()
        articole_noi = data.get("articles", []) if data.get("status") == "ok" else []

        # Dacă nu avem articole noi, păstrăm cele vechi
        if not articole_noi:
            print(f"⚠️ Fără știri noi pentru {category}, păstrez cele salvate")
            return articole_vechi

        # Salvăm noile articole
        cache[cheie_cache] = {
            "articole": articole_noi,
            "data": datetime.now().isoformat()
        }
        salveaza_stiri_noi(cache)
        print(f"✅ Știri noi salvate pentru {category}")
        return articole_noi

    except Exception as e:
        print(f"❌ Eroare: {str(e)} | Afișez știrile salvate")
        return articole_vechi
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
