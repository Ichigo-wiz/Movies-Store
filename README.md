# 🎬 MoviesStore – A Simple Django Web App

MoviesStore is a beginner-friendly Django project designed to showcase basic Django functionality such as user authentication (signup & login) and homepage routing. The project is organized into modular apps – `accounts` for user management and `home` for the main landing page or future movie-related features.

This project is perfect for learning the Django project structure, working with templates, and customizing forms.

---

## 📁 Project Structure

```
moviesstore/
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   │   ├── login.html
│   │   └── signup.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── home/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── moviesstore/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
```

---

## ✅ Features

- 🔐 User Authentication (Signup, Login)
- ✉️ Custom Django Forms
- 🏡 Simple homepage setup
- 🧱 Django template integration
- 🎯 Modular app structure

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/moviesstore.git
cd moviesstore
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Auth Pages

| URL Path            | Description               |
|---------------------|---------------------------|
| `/accounts/login/`  | Login form                |
| `/accounts/signup/` | Registration form         |
| `/`                 | Homepage                  |

---

## 🛠 Technologies Used

- Python 3.x
- Django 4.x
- HTML5, CSS3
- SQLite (default)

---

## 🧑‍💻 Author

**Your Name**  
📧 your.email@example.com  
🔗 [GitHub](https://github.com/your-username)

---

## 📃 License

This project is licensed under the MIT License - see the LICENSE file for details.
