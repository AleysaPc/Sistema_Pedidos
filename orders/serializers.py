from rest_framework import serializers
from .models import Orden, DetalleOrden, HistorialOrden, Notificacion
from restaurants.serializers import ProductoSerializer
from .utils import crear_notificacion

class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DetalleOrden
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    detalles_orden = DetalleOrdenSerializer(many=True, required=False)

    class Meta:
        model = Orden
        fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles_orden', [])
        orden = Orden.objects.create(**validated_data)

        for detalle in detalles_data:
            DetalleOrden.objects.create(
                orden=orden,
                producto_id=detalle['producto_id'],
                cantidad=detalle['cantidad'],
                precio=detalle.get('precio')
            )

        # 🔔 NOTIFICAR RESTAURANTE
        crear_notificacion(
            usuario=orden.restaurante.propietario,
            mensaje=f"🆕 Nuevo pedido {orden.numero_orden}",
            orden=orden
        )

        return orden

class HistorialOrdenSerializer(serializers.ModelSerializer):
    orden_numero = serializers.CharField(source="orden.numero_orden", read_only=True)
    usuario_nombre = serializers.CharField(source="usuario.username", read_only=True)

    class Meta:
        model = HistorialOrden
        fields = "__all__"

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
