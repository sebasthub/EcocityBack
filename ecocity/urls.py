from django.urls import include, path
from rest_framework import routers

from core import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
]
