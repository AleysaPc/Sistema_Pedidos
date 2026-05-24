from rest_framework import viewsets
from .models import Orden, DetalleOrden, HistorialOrden
from .serializers import OrdenSerializer, DetalleOrdenSerializer, HistorialOrdenSerializer
from rest_framework import viewsets
from .models import Notificacion
from .serializers import NotificacionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from orders.utils import crear_notificacion
from rest_framework.permissions import IsAuthenticated

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["estado", "cliente", "restaurante", "repartidor"]

    def perform_update(self, serializer):
        orden = serializer.save()

        # 👇 RESTAURANTE recibe pedido confirmado
        if orden.estado == "ACEPTADO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} fue aceptado"
            )

        if orden.estado == "LISTO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} está listo"
            )

            # 👇 aquí entra el repartidor
            repartidores = orden.restaurante.usuario_set.all() if hasattr(orden.restaurante, "usuario_set") else []

            for r in repartidores:
                crear_notificacion(
                    usuario=r,
                    mensaje=f"Nuevo pedido listo para entrega: {orden.numero_orden}"
                )

class NotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notificacion.objects.filter(usuario=self.request.user).order_by('-fecha')
    
class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer

class Historial_ordenViewSet(viewsets.ModelViewSet):
    queryset = HistorialOrden.objects.all()
    serializer_class = HistorialOrdenSerializer