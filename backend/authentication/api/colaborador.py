from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models.colaborador import Colaborador
from rest_framework import serializers

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ColaboradorModelSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(max_length=50)
    departamento = serializers.CharField(max_length=50)
    entidad = serializers.CharField(max_length=50)
    pais = serializers.CharField(max_length=50)
    siglaEntidad = serializers.CharField(max_length=50)
    unidad = serializers.CharField(max_length=50)

    class Meta:
        model = Colaborador
        fields = ['nombre','departamento','entidad','pais','siglaEntidad','unidad']


    def create(self, validated_data):
        return Colaborador.objects.create(**validated_data)

class ColaboradorView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = ColaboradorModelSerializer

    def get(self, request, format=None):
        user=request.user
        users = Colaborador.objects.filter(id=user.id)
        serializer = ColaboradorModelSerializer(users, many=True)
        return Response(serializer.data)


    def put(self, request):
        serializer = ColaboradorModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = ColaboradorModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
