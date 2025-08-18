from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TestViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'tests', TestViewSet, basename='test')

urlpatterns = [
    path('', include(router.urls)),
]