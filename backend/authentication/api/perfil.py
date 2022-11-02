from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models.perfil import Perfil
from rest_framework import serializers
from rest_framework import status, viewsets


class PerfilModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = '__all__'


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilModelSerializer
    filterset_fields = ['id']
