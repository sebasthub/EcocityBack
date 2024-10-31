from django.db import models
from django.contrib.auth.models import User

class ColetaAgendada(models.Model):
    data = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)