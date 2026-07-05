# ==================================================
# 🔐 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE COD
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
# 📚 TOATE IMPORTURILE - EXACT CE AVEAI + CE TREBUIE
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

# Import pentru știri
try:
    from news_api import get_latest_news
except ImportError:
    print("⚠️ Fișierul news_api.py nu a fost găsit sau nu este corect")
    def get_latest_news(*args, **kwargs):
        return []

# ==================================================
# 🚀 INIȚIALIZARE APLICAȚIE
# ==================================================
app = Flask(__name__)
CORS(app)
load_dotenv()

# ==================================================
# ⏱️ FUNCTIA DE AUTOTREZIRE - PĂSTRATĂ ȘI REPARATĂ
# ==================================================
def keep_alive():
    APP_URL = "https://mypersonalanalyst.com/"
    while True:
        try:
            requests.get(APP_URL, timeout=20)
            print("✅ Autotrezire activă")
        except Exception as e:
            print(f"⚠️ Eroare autotrezire: {e}")
        time.sleep(14 * 60)

# Pornim autotrezirea în siguranță
try:
    threading.Thread(target=keep_alive, daemon=True).start()
except Exception as e:
    print(f"⚠️ Nu s-a putut porni autotrezirea: {e}")

# ==================================================
# 📄 RUTELE APLICAȚIEI - COMPLETE ȘI FĂRĂ ERORI
# ==================================================

# Pagina principală cu știri
@app.route("/")
def home():
    try:
        category = request.args.get("category", "general")
        articles = get_latest_news(category=category, limit=12)
        return render_template("home.html", articles=articles, selected=category)
    except Exception as e:
        print(f"❌ Eroare pe pagina principală: {e}")
        return "⚠️ Eroare la încărcarea paginii", 500

# Pagina Analizor Contracte
@app.route("/contract-analyst")
def contract_analyst():
    try:
        return render_template("contract_analyst.html")
    except Exception as e:
        print(f"❌ Eroare pe contract-analyst: {e}")
        return "⚠️ Eroare la încărcarea paginii", 500

# Pagini legale și suplimentare
@app.route("/termeni")
def termeni():
    try:
        return render_template("termeni.html")
    except:
        return render_template("terms.html")

@app.route("/politica")
def politica():
    try:
        return render_template("politica.html")
    except:
        return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

# ==================================================
# ▶️ PUNERE ÎN FUNCȚIUNE
# ==================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
