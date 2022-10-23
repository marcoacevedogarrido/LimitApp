from django.urls import include, path
from rest_framework.routers import DefaultRouter
from store.api.profiles import ProfileViewSet
from store.api.documentos import DocumentoViewSet
from store.api.facturas import FacturaViewSet


router = DefaultRouter()

router.register(r'store/profiles', ProfileViewSet, basename='profile')
router.register(r'store/documentos', DocumentoViewSet, basename='documento')
router.register(r'store/facturas', FacturaViewSet, basename='factura')

urlpatterns = [
    path('', include(router.urls)),
]
