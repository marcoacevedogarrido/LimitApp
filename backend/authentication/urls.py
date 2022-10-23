from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication.api.users import RegisterView
from authentication.api.users import LoginView
from authentication.api.users import LogoutView

urlpatterns = [
    path(r'api/login', LoginView.as_view()),
    path(r'api/logout', LogoutView.as_view()),
    path(r'api/registro', RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
