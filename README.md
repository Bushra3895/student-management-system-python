# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python) ![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192?style=for-the-badge&logo=postgresql) ![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge)

> A full-stack web-based **Student Management System** built with Python Flask and PostgreSQL. Manage students, track performance, view analytics, and export data — all in one place.

---

## 🌐 Live Demo

👉 **[https://student-management-system-python.onrender.com](https://student-management-system-python.onrender.com)**

> ⚠️ Note: Free instance may take 50 seconds to wake up on first visit.

---

## 📸 Features Overview

| Feature | Description |
|--------|-------------|
| 🔐 Authentication | Secure Register & Login with JWT tokens |
| ➕ Add Students | Add students with roll, name, email, subject, marks & grade |
| ✏️ Edit Students | Update student information anytime via modal |
| 🗑️ Delete Students | Remove students with confirmation prompt |
| 📊 Dashboard | Live stats — total, passed, failed, highest & avg marks |
| 📈 Analytics | Beautiful charts for subject-wise & pass/fail performance |
| 🔍 Search | Instantly search students by name or roll number |
| ⬇️ Export | Download student data as CSV or Excel file |
| 🌙 Dark Mode | Toggle between light and dark theme |
| 📱 Responsive | Works on desktop and mobile browsers |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.14**
- **Flask** — Web framework
- **Flask-JWT-Extended** — JWT authentication
- **Flask-CORS** — Cross-origin requests
- **bcrypt** — Password hashing
- **psycopg2** — PostgreSQL adapter
- **pandas + openpyxl** — CSV & Excel export

### Frontend
- **HTML5, CSS3, Vanilla JavaScript**
- **Chart.js** — Analytics charts
- **Custom CSS** — Dark/Light theme with CSS variables

### Database
- **PostgreSQL** — Hosted on Render

### Deployment
- **Render** — Web Service + PostgreSQL (Free tier)

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Bushra3895/student-management-system-python.git
cd student-management-system-python
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variable
```bash
# Windows
set DATABASE_URL=your_postgresql_connection_url

# Mac/Linux
export DATABASE_URL=your_postgresql_connection_url
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
