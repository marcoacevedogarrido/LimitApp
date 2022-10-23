from django.urls import include, path
from rest_framework.routers import DefaultRouter
from store.api.documentos import DocumentoViewSet
from store.api.facturas import FacturaViewSet


router = DefaultRouter()

router.register(r'api/documentos', DocumentoViewSet, basename='documento')
router.register(r'api/facturas', FacturaViewSet, basename='factura')

urlpatterns = [
    path('', include(router.urls)),
]
