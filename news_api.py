import os
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()

def get_latest_news(category="general", country="gb", limit=12):
    if not NEWS_API_KEY:
        return []

    headers = {"User-Agent": "Mozilla/5.0"}

    if category.lower() == "legal":
        url = "https://newsapi.org/v2/everything?q=law+legal+contract&language=en&pageSize={}&apiKey={}".format(limit, NEWS_API_KEY)
    else:
        url = "https://newsapi.org/v2/top-headlines?category={}&language=en&pageSize={}&apiKey={}".format(category, limit, NEWS_API_KEY)

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        return data.get("articles", []) if data.get("status") == "ok" else []
    except:
        return []
