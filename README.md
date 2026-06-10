# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Render-Live-46E3B7?style=for-the-badge&logo=render)

> A full-featured Student Management System built with Python (Flask) and PostgreSQL, supporting authentication, analytics, dark mode, and data export.

---

## 🌐 Live Demo

🔗 **[https://student-management-system-python.onrender.com/](https://student-management-system-python.onrender.com/)**

> ## 🔑 Demo Credentials

Use the following demo account to explore the application:

**Username:** teacher1

**Password:** pass123

> Note: This is a demo account created for recruiters and reviewers. Feel free to add, edit, or delete sample student records while testing the application.

⚠️ If the application is hosted on Render's free tier, the first request may take 30–60 seconds to load while the server wakes up.


---

## 📌 Project Overview

This Student Management System allows administrators and educators to manage student records efficiently. It started as a simple JSON-based system and evolved into a full-stack application with a PostgreSQL database, secure authentication, and a modern UI.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Secure login/logout with bcrypt password hashing |
| 📋 Student Records | Add, edit, delete, and view student data |
| 📊 Analytics | Dashboard with visual analytics |
| 🌙 Dark Mode | Toggle between light and dark themes |
| 📤 Export | Export student data to CSV/JSON |
| 🗄️ PostgreSQL | Switched from JSON to PostgreSQL for scalability |
| 🚀 Deployment | Hosted on Render with Vercel config support |

---

## 🗂️ Project Structure

```
student-management-system-python/
│
├── api/                  # Flask API routes and endpoints
├── data/                 # Data layer (SQLite/PostgreSQL configs)
├── models/               # Database models
├── services/             # Business logic and service layer
├── templates/            # HTML templates (Jinja2)
│
├── app.py                # Main Flask application entry point
├── database.py           # Database connection and setup (PostgreSQL)
├── requirements.txt      # Python dependencies
├── students.json         # Legacy JSON data (initial version)
├── vercel.json           # Vercel deployment configuration
└── .gitignore            # Git ignored files
```

---

## 🚀 Project Journey — From Start to End

### Phase 1 — Initial Setup
- Created base project structure
- Implemented Student Management System using **JSON file storage**
- Set up `models/` and `services/` directories for clean architecture

### Phase 2 — Feature Development
- Added **SQLite** database support
- Implemented **Authentication** (login/logout) with bcrypt
- Built **Analytics** dashboard
- Added **Dark Mode** toggle
- Enabled **Export** functionality (CSV/JSON)

### Phase 3 — Database Migration
- Switched from SQLite to **PostgreSQL** for production readiness
- Updated `database.py` and `requirements.txt`

### Phase 4 — Deployment & Bug Fixes
- Fixed `memoryview` bcrypt issue in `app.py`
- Resolved `index.html` template conflict
- Refactored Flask app to correctly serve static HTML
- Deployed on **Render** (96 deployments — actively developed!)
- Configured `vercel.json` for Vercel deployment support

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL (production), JSON (legacy)
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templates)
- **Auth:** bcrypt password hashing
- **Deployment:** Render, Vercel
- **Version Control:** Git + GitHub

---

## ⚙️ Local Setup & Installation

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- Git

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/Bushra3895/student-management-system-python.git
cd student-management-system-python
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory and add:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/student_db
SECRET_KEY=your_secret_key_here
```

**5. Run the application**
```bash
python app.py
```

✅ The app will be available at `http://localhost:5000`

---

## 🌍 Deployment Guide — Render

### First-Time Deployment

1. Go to [https://render.com](https://render.com) and sign up/log in
2. Click **"New +"** → Select **"Web Service"**
3. Connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3
5. Add environment variables:
   - `DATABASE_URL` → Your PostgreSQL connection string
   - `SECRET_KEY` → Any random secret string
6. Click **"Create Web Service"**

---
---

## 📦 Dependencies

Key packages from `requirements.txt`:

```
Flask
psycopg2-binary       # PostgreSQL adapter
bcrypt                # Password hashing
python-dotenv         # Environment variable management
gunicorn              # Production WSGI server
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👩‍💻 Author

**Bushra** — [@Bushra3895](https://github.com/Bushra3895)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
