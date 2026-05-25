from .models import HistorialOrden

def crear_historial(orden, usuario, estado):
    HistorialOrden.objects.create(
        orden=orden,
        usuario=usuario,
        estado=estado
    )