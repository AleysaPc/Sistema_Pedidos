from rest_framework import viewsets
from .models import Orden, DetalleOrden, HistorialOrden
from .serializers import OrdenSerializer, DetalleOrdenSerializer, HistorialOrdenSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer

class Historial_ordenViewSet(viewsets.ModelViewSet):
    queryset = HistorialOrden.objects.all()
    serializer_class = HistorialOrdenSerializer