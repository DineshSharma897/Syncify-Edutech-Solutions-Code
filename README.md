# Syncify Student Performance Tracker

A mini backend service built with **Django + Django REST Framework (DRF) + MySQL**.  
This system allows colleges to add students, record their test scores, and fetch performance insights.

---

##  Tech Stack
- **Backend**: Django 5 + Django REST Framework (DRF)
- **Database**: MySQL (connection string provided in task)
- **Python**: 3.10+

---

##  Setup Instructions

### Clone & Install

git clone https://github.com/DineshSharma897/Syncify-Edutech-Solutions-Code.git
cd syncify-student-tracker

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

2️ Database Config
The project is already configured with the provided MySQL database in settings.py:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dineshdb',
        'USER': 'dineshdb',
        'PASSWORD': 'pWmLEeBhisMjRm3p',
        'HOST': '35.232.37.232',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'connect_timeout': 30,
        },
    }
}

If connection issues occur locally, switch to SQLite for testing.

3️ Migrations

python manage.py makemigrations
python manage.py migrate

4️ Run Server
python manage.py runserver
Server runs at: http://127.0.0.1:8000/

API Endpoints
1. Add Student
POST /students/
Body:

json
{
  "name": "Alice",
  "email": "alice@example.com",
  "department": "CSE"
}

2. Add Test Record
POST /tests/
Body:

json
{
  "student": 1,
  "subject": "Math",
  "score": 85,
  "max_score": 100,
  "date": "2025-08-10"
}

3. Student Performance
GET /students/<id>/performance/
Response:

json
{
  "student": "Alice",
  "average_score": 85.0,
  "latest_test": {
    "subject": "Math",
    "score": 85,
    "date": "2025-08-10"
  }
}

4. Top Performers
GET /students/top-performers/?limit=3
Response:

json

  { "student": "Alice", "average_score": 92.0 },
  { "student": "Bob", "average_score": 88.5 },
  { "student": "Charlie", "average_score": 84.3 }

