from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication.api.users import RegisterView
from authentication.api.users import LoginView
from authentication.api.users import LogoutView

urlpatterns = [
    path('authentication/login', LoginView.as_view()),
    path('authentication/logout', LogoutView.as_view()),
    path('authentication/registro', RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
