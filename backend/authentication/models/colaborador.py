from django.db import models
from authentication.models.perfil import Perfil

class Colaborador(models.Model):
    perfil = models.OneToOneField(
        Perfil,
        on_delete=models.CASCADE,
        related_name='usuario',
        default=True,
        null=True
    )
    nombre = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    entidad = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    siglaEntidad = models.CharField(max_length=50, blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']
