# database.py
import sqlite3
import os

DB_PATH = "data/students.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # dict jaisa result milega
    return conn

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = get_connection()
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            roll      TEXT    UNIQUE NOT NULL,
            name      TEXT    NOT NULL,
            email     TEXT,
            subject   TEXT,
            grade     REAL    DEFAULT 0,
            marks     INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role          TEXT DEFAULT 'teacher'
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database ready!")