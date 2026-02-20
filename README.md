# 🌐 Portfolio-Django

A personal portfolio website built using **Django** to showcase projects, skills, and contact information in a clean and professional way.

This project demonstrates Django fundamentals such as routing, template rendering, static file handling, and backend form processing — perfect for students and developers who want a customizable portfolio site.

---

## ✨ Features

- 🧑 About Me section
- 💼 Projects showcase
- 🛠 Skills display
- 📩 Contact form handled by Django backend
- 📱 Responsive design
- ⚙️ Django template inheritance
- 🗂 Organized static & media files
- 🔒 Secure form handling (CSRF protection)

---

## 🧱 Tech Stack

| Technology | Usage |
|----------|------|
| Python | Backend logic |
| Django | Web framework |
| HTML | Page structure |
| CSS | Styling |
| SQLite | Default database |

---

## 📂 Project Structure

Portfolio-Django/
│
├── porf/ # Main Django app
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, images, assets
│ ├── views.py # Request handling
│ ├── models.py # Database models
│ └── urls.py # App routes
│
├── manage.py
├── db.sqlite3
└── .gitignore

---

## 🚀 Installation & Setup

# Clone repository
    git clone https://github.com/Pranavgoli/Portfolio-Django.git
    cd Portfolio-Django

# Create virtual environment
    python -m venv venv

# Activate environment:-

# Windows
    venv\Scripts\activate

# Linux / Mac
    source venv/bin/activate

# Install dependencies
    pip install django

# Apply migrations
    python manage.py migrate

# Run server
    python manage.py runserver

---

🎯 Customization Guide
File	               Purpose
templates/*.html	   Edit content & layout
static/css	         Change styling
models.py	           Add dynamic portfolio data
views.py	           Modify logic
admin.py	           Manage data from admin panel

---

# Create admin user:
    python manage.py createsuperuser

# Admin panel: (Port number can be changed and recommneded to change the port number)
    http://127.0.0.1:8000/admin

---

📌 Future Improvements

Blog section

Resume download

Project filtering

Dark mode toggle

Deployment (Render / Railway / VPS)

PostgreSQL database

REST API integration

---

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

👨‍💻 Author

Pranav Goli

If you like this project ⭐ the repository!

---

# Here are the Project Screenshots For Refernece:-

# Home Page:-
<img width="1918" height="967" alt="image" src="https://github.com/user-attachments/assets/b9fc1cd6-9a0b-48b2-9985-8d960fd13a9e" />

# Django-Admin Page:-
<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/7c3db0a9-12bd-4896-939f-dcc0a2bfc71a" />



