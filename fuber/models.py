from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class vehiculo(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350)


class conductor(models.Model):
    driver_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    vehicle = models.ForeignKey(vehiculo, on_delete=models.CASCADE)


class metodoPago(models.Model):
    payment_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)


class auditory_log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class pasajero_pago(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(metodoPago, on_delete=models.CASCADE)


class viaje(models.Model):
    trip_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(conductor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_origen = models.CharField(max_length=500)
    direccion_destino = models.CharField(max_length=500)
    fecha_viaje = models.DateField()


    