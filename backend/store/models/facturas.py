from django.db import models

class Factura(models.Model):

    rut = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        ordering = ['id']
