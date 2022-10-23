from rest_framework import serializers
from store.models.documentos import Documento
from store.models.facturas import Factura
from rest_framework import viewsets
from rest_framework.response import Response


class FacturaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = '__all__'


class DocumentoModelSerializer(serializers.ModelSerializer):
    factura = FacturaModelSerializer()

    class Meta:
        model = Documento
        fields = '__all__'


class AddDocumentoModelSerializer(serializers.ModelSerializer):

    def create(self, data):
        data = self.context['request'].data
        factura_data = data.pop('factura', None)

        doc = Documento.objects.create(
            **data,
        )

        if factura_data:
            factura = Factura.objects.create(
                **factura_data,
                doc=doc
            )
            doc.factura = factura

        doc.save()
        return doc

    class Meta:
        model = Documento
        fields = '__all__'


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoModelSerializer
    filterset_fields = ['id']

    def create(self, request, *args, **kwargs):
        serializer = AddDocumentoModelSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        doc = serializer.save()
        data = self.get_serializer(doc).data
        return Response(data, status=status.HTTP_201_CREATED)
