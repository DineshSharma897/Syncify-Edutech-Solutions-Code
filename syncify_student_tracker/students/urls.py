from django.urls import path
from .views import StudentCreate, TestCreate, StudentPerformance, TopPerformers

urlpatterns = [
    path("students/", StudentCreate.as_view()),
    path("tests/", TestCreate.as_view()),
    path("students/<int:pk>/performance/", StudentPerformance.as_view()),
    path("students/top-performers/", TopPerformers.as_view()),
]
