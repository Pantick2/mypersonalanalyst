import requests
from dotenv import load_dotenv

# Încarcă cheia API din variabilele de mediu
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

def get_latest_news(category="general", country="gb", limit=15):
    """
    Preia știri din NewsAPI:
    - Pentru categoria Legal: căutare globală după cuvinte cheie
    - Pentru restul categoriilor: întâi știri pe țară, dacă nu sunt, preia știri globale
    """
    if not NEWS_API_KEY:
        print("⚠️ NEWS_API_KEY nu este setată")
        print("⚠️ Eroare: NEWS_API_KEY nu este setată")
        return []

    if category == "legal":
        url = f"https://newsapi.org/v2/everything?q=law+legal+contract+regulation&language=en&sortBy=publishedAt&pageSize={limit}&apiKey={NEWS_API_KEY}"
    headers = {"User-Agent": "MyPersonalAnalyst/1.0"}

    # 🔹 Categoria Legal: căutare globală, nu restricționată pe țară
    if category.lower() == "legal":
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q=law+legal+contract+regulation+business+dispute&"
            f"language=en&sortBy=publishedAt&pageSize={limit}&apiKey={NEWS_API_KEY}"
        )
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"
        # 🔹 Întâi încercăm știri pe țară
        url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"country={country}&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"
        )

    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return data.get("articles", []) if data.get("status") == "ok" else []
        response = requests.get(url, headers=headers, timeout=12)
        data = response.json()

        # Dacă nu avem rezultate pe țară, luăm știri globale pentru categoria respectivă
        if data.get("status") == "ok" and len(data.get("articles", [])) == 0 and category != "legal":
            print(f"ℹ️ Nu sunt știri pe țară pentru {category}, preluăm din surse globale...")
            url = (
                f"https://newsapi.org/v2/top-headlines?"
                f"category={category}&language=en&pageSize={limit}&apiKey={NEWS_API_KEY}"
            )
            response = requests.get(url, headers=headers, timeout=12)
            data = response.json()

        if data.get("status") == "ok":
            return data.get("articles", [])
        else:
            print(f"⚠️ Răspuns NewsAPI: {data.get('message', 'Eroare necunoscută')}")
            return []

    except Exception as e:
        print("Eroare preluare știri:", e)
        print(f"❌ Eroare conexiune NewsAPI: {str(e)}")
        return []
