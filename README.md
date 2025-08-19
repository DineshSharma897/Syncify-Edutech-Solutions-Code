# Student Performance Tracking API (Django + DRF + MySQL)

##  Project Overview
This project is a backend API built with **Django REST Framework** and **MySQL** to manage student performance.  
It allows you to:  
- Add students  
- Record their test results  
- Calculate their average scores  
- Fetch the latest test performance  
- Retrieve **Top Performers** using both **ORM** and **Raw SQL**

---

## Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: MySQL  
- **Language**: Python 3  
- **Tools**: Postman for API testing  

---

##  Project Structure
```
student_service/
│── manage.py
│── student_service/        # Project settings
│── api/                    # Main app
│   │── models.py           # Student & Test models
│   │── serializers.py      # DRF serializers
│   │── views.py            # API views (CRUD + custom endpoints)
│   │── urls.py             # API routes
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


### 2 Configure Database (MySQL)
In `student_service/settings.py`, update:
```python
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
            'autocommit': True, 
            'connect_timeout': 30, 
            'ssl_disabled': False, 
            'ssl_verify_cert': False, 
            'ssl_verify_identity': False, 
            # Removed 'auth_plugin': 'mysql_native_password' - this parameter is causing the error 
} 
} 
} 
```

### 4️3 Apply migrations

python manage.py makemigrations
python manage.py migrate


### 5️4 Run the server

python manage.py runserver


---

##  API Endpoints

### Student APIs
- `POST /api/students/` → Add a new student  
- `GET /api/students/` → List all students  
- `GET /api/students/{id}/performance/` → Get average score & latest test for a student  

### Test APIs
- `POST /api/tests/` → Add a new test result   

### Top Performers
- `GET /api/students/top-performers/?limit=3` → Fetch top students (using ORM)  
- `GET /api/students/top-performers-sql/?limit=3` → Fetch top students (using raw SQL)  

---

### Example Responses

### Create Student
Request:
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "department": "CSE"
}
```

Response:
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "department": "CSE"
}
```

### Top Performers
```json
[
  {"student": "Alice", "average_score": 85.5},
  {"student": "Bob", "average_score": 78.0}
]
```

---

## Bonus
- Implemented **Raw SQL Query** (`top-performers-sql`) to fetch top students directly using SQL joins and aggregation.  
- Shows flexibility of using both **ORM** and **SQL** approaches.  

---

