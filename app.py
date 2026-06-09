from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "students.json"

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f)

@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    students = load_students()
    students.append(data)
    save_students(students)
    return jsonify({"message": "Student added!"})

@app.route("/delete/<string:roll>", methods=["DELETE"])
def delete_student(roll):
    students = load_students()
    students = [s for s in students if s['roll'] != roll]
    save_students(students)
    return jsonify({"message": "Deleted!"})

if __name__ == "__main__":
    app.run(debug=True)