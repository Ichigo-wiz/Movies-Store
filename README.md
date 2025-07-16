# 🎬 MoviesStore – A Simple Django Web App

MoviesStore is a beginner-friendly Django project designed to showcase basic Django functionality such as user authentication (signup & login) and homepage routing.
The project is organized into modular apps – `accounts` for user management and `home` for the main landing page or future movie-related features.

This project is perfect for learning the Django project structure, working with templates, and customizing forms.

---

## 📸 Screenshots

> *Login Page*

![Login Page](screenshots/login.png)

> *Signup Page*

![Signup Page](screenshots/signup.png)

> *(Optional)* Add homepage screenshot

---

## 📁 Project Structure
moviesstore/
├── accounts/ # Handles login/signup
│ ├── templates/accounts/
│ │ ├── login.html
│ │ └── signup.html
│ ├── forms.py
│ ├── urls.py
│ └── views.py
│ ...
├── home/ # Home page app
│ ├── urls.py
│ └── views.py
│ ...
├── db.sqlite3 # SQLite DB
├── manage.py # Django entrypoint
├── moviesstore/ # Main project config
---

## ✅ Features

- 🔐 User Authentication (Signup, Login)
- ✉️ Custom Django Forms
- 🏡 Simple homepage setup
- 🧱 Django template integration
- 🎯 Modular app structure

---


