from django.urls import include, path
from rest_framework import routers

from core import views


router = routers.DefaultRouter()
router.register('users', views.UserList)
router.register('coleta-agendada', views.ColetaAgendadaList)


urlpatterns = [
    path('', include(router.urls)),
]
