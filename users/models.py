from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('CLIENT', 'Client'),
        ('REPARTIDOR', 'Repartidor'),
        ('ADMIN_RESTAURANT', 'Admin Restaurant')
    )

    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    ci = models.CharField(max_length=15)
    rol = models.CharField(max_length=20, choices=ROLES, default='CLIENT')

    def __str__(self):
        return self.username