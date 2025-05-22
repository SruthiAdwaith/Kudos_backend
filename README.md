# 🎉 Kudos Backend API

A Django REST API for sending kudos (appreciation) within an organization.
Each user can send up to **3 kudos per week**, and kudos do **not accumulate**.

---

## 🚀 Features

- ✅ JWT-based authentication
- ✅ Weekly kudos limit per user
- ✅ Send kudos with messages
- ✅ View kudos received
- ✅ View user details & organization
- ✅ View kudos remaining this week

---

## 🏗️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- SimpleJWT
- CORS Headers

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
#create the folder and clone to the folder
git clone  https://github.com/SruthiAdwaith/Kudos_backend.git


# create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

#Install Dependencies
pip install -r requirements.txt


#Apply Migrations
python manage.py makemigrations
python manage.py migrate

#Create Super User
python manage.py createsuperuser


#Run the server
python manage.py runserver
