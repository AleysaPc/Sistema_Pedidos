from rest_framework import serializers
from .models import Orden, DetalleOrden, HistorialOrden

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    #Permite ver los detalles de la orden cuando se consulta una orden
    detalle_orden = DetalleOrdenSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = '__all__'

class HistorialOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialOrden
        fields = '__all__'
