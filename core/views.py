from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from core.serializers import UserSerializer, ColetaAgendadaSerializer
from rest_framework import generics
from core.models import ColetaAgendada

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
class ColetaAgendadaList(viewsets.ModelViewSet):
    queryset = ColetaAgendada.objects.all()
    serializer_class = ColetaAgendadaSerializer
    permission_classes = [permissions.AllowAny]