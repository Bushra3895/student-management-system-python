# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![HTML](https://img.shields.io/badge/HTML5-Frontend-orange?style=for-the-badge&logo=html5)
![CSS](https://img.shields.io/badge/CSS3-Styling-blue?style=for-the-badge&logo=css3)
![JSON](https://img.shields.io/badge/JSON-Data%20Storage-lightgrey?style=for-the-badge&logo=json)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)

> A clean and responsive web-based Student Management System built with Python Flask. Manage student records with ease — add, view, and track students all in one place.

## 🌐 Live Demo

🔗 **[View Live Project](https://student-management-system-python-o6.vercel.app/)**


---

## ✨ Features

- ➕ **Add New Students** — Enter student name, roll number, and grade
- 📊 **Dashboard Counter** — Instantly see total number of students
- 🗂️ **JSON Data Storage** — Lightweight file-based data persistence
- 🎨 **Clean UI** — Simple and user-friendly interface
- 📱 **Responsive Design** — Works on all screen sizes
- ⚡ **Fast Performance** — Lightweight Flask backend

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Data Storage | JSON |
| Architecture | MVC (Models, Services, Templates) |
| Deployment | Vercel |

---

## 📁 Project Structure

```
student_management_system/
│
├── data/
│   └── students.json          # Student data storage
│
├── models/
│   └── student.py             # Student model/schema
│
├── services/
│   └── student_service.py     # Business logic layer
│
├── templates/
│   └── index.html             # Frontend HTML template
│
├── app.py                     # Flask application entry point
├── main.py                    # Main runner
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine.

```bash
python --version
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Bushra3895/student-management-system-python.git
cd student-management-system-python
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://127.0.0.1:5000/
```

---

## 📋 How to Use

1. Open the app in your browser
2. Fill in the **Student Name**, **Roll Number**, and **Grade** fields
3. Click **Add Student** button
4. The student is saved and the total count updates automatically

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page — view all students |
| POST | `/add` | Add a new student |

---

## 📦 Dependencies

```txt
Flask
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 🌱 Future Improvements

- [ ] Edit and delete student records
- [ ] Search and filter functionality
- [ ] Export data to CSV/Excel
- [ ] User authentication
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Student grade analytics dashboard

---

## 👩‍💻 Author

**Bushra**
- GitHub: [@Bushra3895](https://github.com/Bushra3895)
- Project Link: [student-management-system-python](https://github.com/Bushra3895/student-management-system-python)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, please give it a star!** ⭐
