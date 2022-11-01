from .api.users import ListUsers, RegisterView, ProfileView
from django.urls import path
from .api.colaborador import ColaboradorView

urlpatterns = [
    path('api/usuarios', ListUsers.as_view()),
    path('api/registro', RegisterView.as_view()),
    path('api/colaborador', ColaboradorView.as_view()),
    path('api/perfil', ProfileView.as_view()),
]
