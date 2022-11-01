from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models.colaborador import Colaborador
from rest_framework import serializers
from rest_framework import status, viewsets


class ColaboradorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colaborador
        fields = ['nombre','departamento','entidad','pais','siglaEntidad','unidad']


class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorModelSerializer
    filterset_fields = ['id']
