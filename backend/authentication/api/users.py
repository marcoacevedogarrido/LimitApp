
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

class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=3)
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class ListUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user=request.user
        users = User.objects.filter(id=user.id)
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)


class UserSignUpSerializer(serializers.Serializer):
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
    serializer_class = UserSignUpSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserModelSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

    def update(self, instance, validated_data):
        validated_data.pop('email', None)               # prevenimos el borrado
        return super().update(instance, validated_data)


def validate_password(self, value):
    return make_password(value)

def validate_username(self, value):
    value = value.replace(" ", "")  # Ya que estamos borramos los espacios
    try:
        user = get_user_model().objects.get(username=value)
        # Si es el mismo usuario mandando su mismo username le dejamos
        if user == self.instance:
            return value
    except get_user_model().DoesNotExist:
        return value
    raise serializers.ValidationError("Nombre de usuario en uso")

def validate_email(self, value):
    # Hay un usuario con este email ya registrado?
    try:
        user = get_user_model().objects.get(email=value)
    except get_user_model().DoesNotExist:
        return value
    # En cualquier otro caso la validación fallará
    raise serializers.ValidationError("Email en uso")
