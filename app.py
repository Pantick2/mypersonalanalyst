# ==================================================
# ## 🔐 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE COD
# ==================================================
SEMNATURA_OBLIGATORIE = "IULIAN_ICHIM_UNGUREANU"
try:
    with open(__file__, "r", encoding="utf-8") as f:
        if "IULIAN_ICHIM_UNGUREANU" not in f.read():
            import sys
            sys.exit("❌ EROARE: Licență invalidă sau cod modificat neautorizat!")
except Exception:
    pass

# ==================================================
# 📚 TOATE IMPORTURILE - EXACT CE AVEAI
# ==================================================
import os
import time
import threading
import requests
from flask import Flask, render_template, request, jsonify
from google import genai
import pypdf
import docx
import openpyxl
from flask_cors import CORS
from dotenv import load_dotenv
from news_api import get_latest_news

# ==================================================
# 🚀 INIȚIALIZARE APLICAȚIE
# ==================================================
app = Flask(__name__)
CORS(app)  # Păstrăm CORS activ
load_dotenv()  # Încarcă variabilele din mediu

# ==================================================
# ⏱️ FUNCTIA DE AUTOTREZIRE - PENTRU A NU ADOARMI INSTANȚA
# ==================================================
def keep_alive():
    APP_URL = "https://mypersonalanalyst.com/"
    while True:
        try:
            requests.get(APP_URL, timeout=20)
            print("✅ Autotrezire activă")
        except Exception as e:
            print(f"⚠️ Eroare autotrezire: {e}")
        time.sleep(14 * 60)  # Verifică la fiecare 14 minute

# Pornim firul separat
threading.Thread(target=keep_alive, daemon=True).start()

# ==================================================
# 📄 RUTELE APLICAȚIEI
# ==================================================

# Pagina principală cu știri
@app.route("/")
def home():
    category = request.args.get("category", "general")
    articles = get_latest_news(category=category, limit=12)
    return render_template("home.html", articles=articles, selected=category)

# --- AICI RUTELE PE CARE LE AVEAI DEJA ---
@app.route("/contract-analyst")
def contract_analyst():
    return render_template("contract_analyst.html")

@app.route("/termeni")
def termeni():
    return render_template("termeni.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

# 📌 Dacă ai și alte rute în codul tău, le lași așa cum sunt aici, nu le ștergem

# ==================================================
# ▶️ PUNERE ÎN FUNCȚIUNE
# ==================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
