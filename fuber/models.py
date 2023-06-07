from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class vehiculo(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    placa = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=350)

    def __str__(self):
        return self.placa   


class conductor(models.Model):
    driver_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    vehicle = models.OneToOneField(vehiculo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


class metodoPago(models.Model):
    payment_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.marca + ' -> ' + self.tipo


class auditory_log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class viaje(models.Model):
    trip_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(conductor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_origen = models.CharField(max_length=500)
    direccion_destino = models.CharField(max_length=500)
    fecha_viaje = models.DateField()


    