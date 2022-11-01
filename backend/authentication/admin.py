from django.contrib import admin
from .models.colaborador import Colaborador
from .models.jefatura import Jefatura
from .models.supervisor import Supervisor

admin.site.register(Colaborador)
admin.site.register(Jefatura)
admin.site.register(Supervisor)
