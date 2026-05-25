from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Orden, DetalleOrden, HistorialOrden, Notificacion
from .serializers import OrdenSerializer, DetalleOrdenSerializer, HistorialOrdenSerializer, NotificacionSerializer

from orders.utils import crear_notificacion
from orders.services import crear_historial
from users.models import User


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["estado", "cliente", "restaurante", "repartidor"]

    def perform_update(self, serializer):
        request_user = self.request.user
        orden = serializer.save()

        # 🔥 HISTORIAL (SIEMPRE)
        crear_historial(orden, request_user, orden.estado)

        # =========================
        # CLIENTE
        # =========================
        if orden.estado == "ACEPTADO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} fue ACEPTADO",
                orden=orden
            )

        elif orden.estado == "PREPARANDO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} está en preparación",
                orden=orden
            )

        elif orden.estado == "LISTO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} está LISTO",
                orden=orden
            )

            # repartidores
            repartidores = User.objects.filter(rol='REPARTIDOR')

            for r in repartidores:
                crear_notificacion(
                    usuario=r,
                    mensaje=f"Pedido disponible: {orden.numero_orden}",
                    orden=orden
                )

        elif orden.estado == "EN_CAMINO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} va en camino",
                orden=orden
            )

        elif orden.estado == "ENTREGADO":
            crear_notificacion(
                usuario=orden.cliente,
                mensaje=f"Tu pedido {orden.numero_orden} fue ENTREGADO",
                orden=orden
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


class HistorialOrdenViewSet(viewsets.ModelViewSet):
    serializer_class = HistorialOrdenSerializer
    queryset = HistorialOrden.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = HistorialOrden.objects.all()

        orden_id = self.request.query_params.get("orden_id")

        # 🔍 FILTRO POR CODIGO DE ORDEN (ORD-XXXX)
        if orden_id:
            return queryset.filter(
                orden__numero_orden__icontains=orden_id.strip()
            ).order_by("-fecha")

        # 👤 CLIENTE
        if user.rol == "CLIENT":
            return queryset.filter(
                orden__cliente=user
            ).order_by("-fecha")

        # 🚚 REPARTIDOR
        if user.rol == "REPARTIDOR":
            return queryset.filter(
                orden__repartidor=user
            ).order_by("-fecha")

        # 🏪 ADMIN RESTAURANTE
        if user.rol == "ADMIN_RESTAURANT":
            return queryset.filter(
                orden__restaurante__propietario=user
            ).order_by("-fecha")

        return HistorialOrden.objects.none()