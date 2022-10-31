from .api.users import ListUsers, RegisterView
from django.urls import path


urlpatterns = [
    path('api/usuarios', ListUsers.as_view()),
    path('api/registro', RegisterView.as_view()),
]
