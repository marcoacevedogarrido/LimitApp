from rest_framework import serializers
from store.models.facturas import Factura
from rest_framework import viewsets
from rest_framework.response import Response


class FacturaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = (
            "rut",
        )


class AddFacturaModelSerializer(serializers.ModelSerializer):

    def create(self, data):
        data = self.context['request'].data

        doc = Factura.objects.create(
            **data,
        )
        doc.save()
        return doc

    class Meta:
        model = Factura
        fields = '__all__'


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaModelSerializer
    filterset_fields = ['id']

    def create(self, request, *args, **kwargs):
        serializer = AddFacturaModelSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        doc = serializer.save()
        data = self.get_serializer(doc).data
        return Response(data, status=status.HTTP_201_CREATED)
