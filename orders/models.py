from django.db import models
from users.models import User
from restaurants.models import Restaurante, Producto
import random
import string

class Orden(models.Model):
    def generar_numero_orden():
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = random.randint(100, 999)
        return f"ORD-{letras}{numeros}"
    
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('ACEPTADO', 'Aceptado'),
        ('PREPARANDO', 'Preparando'),
        ('LISTO', 'Listo'),
        ('EN_CAMINO', 'En Camino'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    )

    METODOS_PAGO = (
        ('EFECTIVO', 'Efectivo'),
        ('QR', 'QR'),
    )

    ESTADOS_PAGO = (
        ('PENDIENTE', 'Pendiente'),
        ('SALDO_PENDIENTE', 'Saldo pendiente'),
        ('PAGADO', 'Pagado'),
    )

    numero_orden = models.CharField(max_length=50, unique=True, default=generar_numero_orden, editable=False)
    cliente = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='ordenes_cliente')
    restaurante = models.ForeignKey('restaurants.Restaurante', on_delete=models.CASCADE, related_name='ordenes_restaurante')
    repartidor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='ordenes_repartidor', null=True, blank=True)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='PENDIENTE')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='PENDIENTE')

    
    def __str__(self):
        return self.numero_orden
    
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles_orden')
    producto = models.ForeignKey('restaurants.Producto', on_delete=models.CASCADE, related_name='detalles_producto')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.orden.numero_orden}"

class HistorialOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    estado = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estado}"
    
class Notificacion(models.Model):
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    orden = models.ForeignKey('orders.Orden', on_delete=models.CASCADE, null=True, blank=True)
