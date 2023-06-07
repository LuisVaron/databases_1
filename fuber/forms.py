from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class userForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class driverForm(ModelForm):
    class Meta:
        model = conductor
        fields = '__all__'

class tripForm(ModelForm):
    class Meta:
        model = viaje
        fields = '__all__'

class vehicleForm(ModelForm):
    class Meta:
        model = vehiculo
        fields = '__all__'

class paymentForm(ModelForm):
    class Meta:
        model = metodoPago
        fields = '__all__'
