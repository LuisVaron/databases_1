from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class vehiculo(models.Model):
    vehicleId = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350)


class conductor(models.Model):
    driverId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    fechaNacimiento = models.DateField()
    vehicleId = models.ForeignKey(vehiculo, on_delete=models.CASCADE)


class metodoPago(models.Model):
    paymentId = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)


class auditory_log(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class pasajero_pago(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentId = models.ForeignKey(metodoPago, on_delete=models.CASCADE)


class viaje(models.Model):
    tripId = models.AutoField(primary_key=True)
    driverId = models.ForeignKey(conductor, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    direccionOrigen = models.CharField(max_length=500)
    direccionDestino = models.CharField(max_length=500)
    fechaViaje = models.DateField()


    