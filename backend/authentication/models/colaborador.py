from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):

    usuariocolaborador = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
