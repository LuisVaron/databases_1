from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class userForm(ModelForm):
    payment_method = forms.MultipleChoiceField(choices=[(opcion.payment_id, opcion.marca+' -> '+opcion.tipo) for opcion in metodoPago.objects.all()], required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'last_login', 'groups', 'email', 'is_active', 'is_superuser', 'date_joined', 'payment_method']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_login': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_joined': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': False})
        }


class createUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class driverForm(ModelForm):

    class Meta:
        model = conductor
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'fecha_nacimiento', 'vehicle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'})
        }
        

class tripForm(ModelForm):
    class Meta:
        model = viaje
        fields = ['driver', 'user', 'direccion_origen', 'direccion_destino', 'fecha_viaje']
        widgets = {
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'direccion_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_destino': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_viaje': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class vehicleForm(ModelForm):
    class Meta:
        model = vehiculo
        fields = ['marca', 'color', 'descripcion']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'})
        }


class createVehicleForm(ModelForm):
    class Meta:
        model = vehiculo
        fields = ['placa', 'marca', 'color', 'descripcion']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'})
        }


class paymentForm(ModelForm):
    class Meta:
        model = metodoPago
        fields = ['marca', 'tipo']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'})
        }
