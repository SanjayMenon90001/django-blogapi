# Django-Blogapi
# 📝 Django Blog API

A RESTful Blog API built using **Django** and **Django REST Framework** that supports:
- User authentication
- Blog post creation, editing, and deletion
- Nested comments
- Custom permissions (owner-only editing)
- Pagination, filtering, searching, and ordering
- Admin panel customization
- Unit testing using `APITestCase` and `factory_boy`

---

## 🚀 Features

✅ Full CRUD for Blog Posts  
✅ Nested Comments per Post  
✅ Authenticated-only post/comment creation  
✅ Custom permission: Only the owner can edit/delete  
✅ Pagination, Filtering, Search, and Ordering  
✅ Django Admin panel with list filters and search  
✅ API test coverage using `factory_boy` and DRF `APITestCase`  
✅ Clean project structure with `requirements.txt`  
✅ GitHub integrated with full version control

---

## 🏗️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- django-filter
- factory_boy (for test data generation)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/SanjayMenon90001/django-blogapi.git

cd django-blogapi

### 2.Create and Activate a Virtual Environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Requirements

pip install -r requirements.txt

### 4. Apply Migrations and Create Superuser

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

### 5. Run the Server

python manage.py runserver


