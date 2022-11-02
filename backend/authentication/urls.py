from .api.users import UsuarioView, RegisterView
from django.urls import path, include
from .api.colaborador import ColaboradorViewSet
from .api.perfil import PerfilViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api/colaborador', ColaboradorViewSet, basename='colaborador')
router.register(r'api/perfil', PerfilViewSet, basename='perfil')

urlpatterns = [
    path('', include(router.urls)),
    path('api/usuario', UsuarioView.as_view()),
    path('api/registro', RegisterView.as_view()),
]
