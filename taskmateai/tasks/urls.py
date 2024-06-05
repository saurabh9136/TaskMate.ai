from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskAPI

router = DefaultRouter()
router.register(r'tasks', TaskAPI, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
]
