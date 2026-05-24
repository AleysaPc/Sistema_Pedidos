from .models import Notificacion

def crear_notificacion(usuario, mensaje, orden=None):
    Notificacion.objects.create(
        usuario=usuario,
        mensaje=mensaje,
        orden=orden
    )