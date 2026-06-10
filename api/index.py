from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="../templates")

@app.route("/")
def index():
    return send_from_directory("../templates", "index.html")

handler = app
