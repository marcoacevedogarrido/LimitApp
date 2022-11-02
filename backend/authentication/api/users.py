from django.contrib.auth import password_validation, authenticate
from rest_framework import status, viewsets, permissions
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .colaborador import ColaboradorModelSerializer
from authentication.models.colaborador import Colaborador


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        return instance


class UsuarioView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

    def create(self, request, *args, **kwargs):
        serializer = UserModelSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        data = self.get_serializer(User).data
        return Response(data, status=status.HTTP_201_CREATED)


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(min_length=2, max_length=50, write_only=True)
    last_name = serializers.CharField(min_length=2, max_length=100)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=4,max_length=20,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)


    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
