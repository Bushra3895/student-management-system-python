from flask import Flask, render_template, request, jsonify
import os
import urllib.request
import json

app = Flask(__name__, template_folder="../templates")

JSONBIN_BIN_ID  = os.environ.get("JSONBIN_BIN_ID", "")
JSONBIN_API_KEY = os.environ.get("JSONBIN_API_KEY", "")
BASE_URL = f"https://api.jsonbin.io/v3/b/{JSONBIN_BIN_ID}"
HEADERS = {
    "X-Master-Key": JSONBIN_API_KEY,
    "Content-Type": "application/json",
    "X-Bin-Versioning": "false",
}

def _request(method, url, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def load_students():
    try:
        result = _request("GET", BASE_URL)
        return result.get("record", {}).get("students", [])
    except:
        return []

def save_students(students):
    try:
        _request("PUT", BASE_URL, {"students": students})
    except:
        pass

@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    if not data or not data.get("name") or not data.get("roll"):
        return jsonify({"error": "Name aur Roll zaroori hai!"}), 400
    students = load_students()
    if any(s["roll"] == data["roll"] for s in students):
        return jsonify({"error": "Roll number pehle se hai!"}), 409
    students.append({
        "name": data.get("name", "").strip(),
        "roll": data.get("roll", "").strip(),
        "grade": data.get("grade", "").strip(),
    })
    save_students(students)
    return jsonify({"message": "Student add ho gaya!"})

@app.route("/delete/<string:roll>", methods=["DELETE"])
def delete_student(roll):
    students = load_students()
    new_list = [s for s in students if s["roll"] != roll]
    if len(new_list) == len(students):
        return jsonify({"error": "Student nahi mila!"}), 404
    save_students(new_list)
    return jsonify({"message": "Deleted!"})

handler = app
