<<<<<<< HEAD
# app.py
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt
import pandas as pd
import io
import os
from database import get_connection, init_db
=======
from flask import Flask, render_template, request, jsonify
import os
import urllib.request
import urllib.error
import json
>>>>>>> 4857efeec9d3642edf45eb047e4a2e6c3246f910

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
# JWT Config
app.config["JWT_SECRET_KEY"] = "student-secret-2024"  # baad mein .env mein daalna
jwt = JWTManager(app)

# DB initialize karo app start pe
init_db()

# ─────────────────────────────────────────
# 🔐 AUTH ROUTES
# ─────────────────────────────────────────

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    try:
        conn = get_connection()
        conn.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (data["username"], hashed, data.get("role", "teacher"))
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "User registered!"})
    except:
        return jsonify({"error": "Username already exists"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (data["username"],)
    ).fetchone()
    conn.close()
    
    if user and bcrypt.checkpw(data["password"].encode(), user["password_hash"]):
        token = create_access_token(identity=data["username"])
        return jsonify({"token": token, "username": data["username"]})
    return jsonify({"error": "Wrong username or password"}), 401

# ─────────────────────────────────────────
# 👤 STUDENT ROUTES
# ─────────────────────────────────────────
=======
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
>>>>>>> 4857efeec9d3642edf45eb047e4a2e6c3246f910

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students", methods=["GET"])
@jwt_required()
def get_students():
    conn = get_connection()
    students = conn.execute("SELECT * FROM students ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(s) for s in students])

@app.route("/add", methods=["POST"])
@jwt_required()
def add_student():
    data = request.json
<<<<<<< HEAD
    try:
        conn = get_connection()
        conn.execute(
            "INSERT INTO students (roll, name, email, subject, grade, marks) VALUES (?,?,?,?,?,?)",
            (data["roll"], data["name"], data.get("email",""),
             data.get("subject",""), data.get("grade", 0), data.get("marks", 0))
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Student added!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/update/<roll>", methods=["PUT"])
@jwt_required()
def update_student(roll):
    data = request.json
    conn = get_connection()
    conn.execute(
        "UPDATE students SET name=?, email=?, subject=?, grade=?, marks=? WHERE roll=?",
        (data["name"], data.get("email",""), data.get("subject",""),
         data.get("grade", 0), data.get("marks", 0), roll)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated!"})

@app.route("/delete/<roll>", methods=["DELETE"])
@jwt_required()
def delete_student(roll):
    conn = get_connection()
    conn.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted!"})

# ─────────────────────────────────────────
# 📊 ANALYTICS ROUTE
# ─────────────────────────────────────────

@app.route("/analytics", methods=["GET"])
@jwt_required()
def analytics():
    conn = get_connection()
    data = conn.execute('''
        SELECT 
            COUNT(*)                                          AS total,
            ROUND(AVG(marks), 1)                             AS avg_marks,
            MAX(marks)                                        AS highest,
            MIN(marks)                                        AS lowest,
            SUM(CASE WHEN marks >= 50 THEN 1 ELSE 0 END)    AS passed,
            SUM(CASE WHEN marks < 50  THEN 1 ELSE 0 END)    AS failed
        FROM students
    ''').fetchone()
    
    subjects = conn.execute('''
        SELECT subject, ROUND(AVG(marks),1) as avg_marks, COUNT(*) as count
        FROM students GROUP BY subject
    ''').fetchall()
    conn.close()
    
    return jsonify({
        "overview": dict(data),
        "by_subject": [dict(s) for s in subjects]
    })

# ─────────────────────────────────────────
# 📥 EXPORT ROUTES
# ─────────────────────────────────────────

@app.route("/export/csv", methods=["GET"])
@jwt_required()
def export_csv():
    conn = get_connection()
    df = pd.read_sql("SELECT roll, name, email, subject, grade, marks FROM students", conn)
    conn.close()
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="students.csv"
    )

@app.route("/export/excel", methods=["GET"])
@jwt_required()
def export_excel():
    conn = get_connection()
    df = pd.read_sql("SELECT roll, name, email, subject, grade, marks FROM students", conn)
    conn.close()
    output = io.BytesIO()
    df.to_excel(output, index=False, sheet_name="Students")
    output.seek(0)
    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="students.xlsx"
    )

if __name__ == "__main__":
    app.run(debug=True)
=======
    if not data or not data.get("name") or not data.get("roll"):
>>>>>>> 4857efeec9d3642edf45eb047e4a2e6c3246f910
