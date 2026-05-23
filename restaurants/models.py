from django.db import models
from users.models import User

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    nit = models.CharField(max_length=15)

    propietario = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    restaurante = models.ForeignKey(
        Restaurante, on_delete=models.CASCADE
    )

    nombre_producto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    disponibilidad = models.BooleanField(default=True)

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre_producto