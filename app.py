from flask import Flask, render_template, request, jsonify
import os
import urllib.request
import urllib.error
import json

app = Flask(__name__)

JSONBIN_BIN_ID  = os.environ.get("JSONBIN_BIN_ID",  "YOUR_BIN_ID_HERE")
JSONBIN_API_KEY = os.environ.get("JSONBIN_API_KEY", "YOUR_API_KEY_HERE")

BASE_URL = f"https://api.jsonbin.io/v3/b/{JSONBIN_BIN_ID}"
HEADERS  = {
    "X-Master-Key"  : JSONBIN_API_KEY,
    "Content-Type"  : "application/json",
    "X-Bin-Versioning": "false",
}

def _request(method, url, body=None):
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def load_students():
    try:
        result = _request("GET", BASE_URL)
        return result.get("record", {}).get("students", [])
    except Exception as e:
        print(f"[load_students] error: {e}")
        return []

def save_students(students):
    try:
        _request("PUT", BASE_URL, {"students": students})
    except Exception as e:
        print(f"[save_students] error: {e}")

@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    if not data or not data.get("name") or not data.get("roll"):
