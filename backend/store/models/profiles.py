from django.db import models
from store.utils.models import StoreModel

class Profile(StoreModel):

    razon_social = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=0
    )
    name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=0
    )
    rut = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
