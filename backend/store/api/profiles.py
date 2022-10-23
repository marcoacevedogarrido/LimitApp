from rest_framework import serializers
from store.models.profiles import Profile
from rest_framework import viewsets


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "razon_social",
            "name",
            "rut"
        )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer
    filterset_fields = ['id']
