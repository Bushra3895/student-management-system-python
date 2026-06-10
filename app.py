# app.py
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt
import pandas as pd
import io
import os
from database import get_connection, init_db

app = Flask(__name__)
CORS(app)

# JWT Config
app.config["JWT_SECRET_KEY"] = "student-secret-2024"
jwt = JWTManager(app)

# DB initialize karo app start pe
init_db()

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
    app.run(debug=False, host="0.0.0.0")