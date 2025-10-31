# 📚 Django LMS (Learning Management System)

A simple **Learning Management System** built with **Django** for managing students, teachers, and admins — with authentication, dashboards, and role-based access.

## 🚀 Live Demo
👉 [Visit Deployed App](https://lms-django-66hw.onrender.com/)

---

## 🧩 Features
✅ User authentication (Admin / Teacher / Student)  
✅ Role-based dashboard views  
✅ Simple and clean UI with Bootstrap / Tailwind  
✅ Admin can manage users  
✅ Teacher can view their dashboard  
✅ Student can view their dashboard  
✅ Logout and navigation included  

---

## 🏗️ Tech Stack
- **Frontend:** HTML, Bootstrap (or Tailwind)
- **Backend:** Django 5.2.7
- **Database:** SQLite (default)
- **Server:** Gunicorn + Render
- **Static Files:** WhiteNoise

---

## ⚙️ Installation (For Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahbaraalam/lms-django.git
   cd lms-django

2. Create a virtual environment
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Run the development server
   python manage.py runserver

open - http://localhost:8000/

Deployment (on Render)
Added gunicorn as production server
Configured WhiteNoise for static files
Used dj-database-url for flexible DB config
Deployment command:
    gunicorn lms_project.wsgi

Project Structure
lms-django/
│
├── accounts/
│   ├── templates/accounts/
│   ├── views.py
│   ├── urls.py
│
├── lms_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   ├── home.html
│   ├── base.html
│
├── staticfiles/
│
├── manage.py
└── requirements.txt

Author

Rahbar Aalam
📧 rahbaraalam608@gmail.com