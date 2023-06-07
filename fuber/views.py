from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['email']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': '''<div class="alert alert-danger" role="alert">
                    Try again! Username already exists.
                    </div>'''
                })

        return render(request, 'signup.html', {
            'error': '''<div class="alert alert-danger" role="alert">
                    Try again! Password do not match.
                    </div>'''
        })


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    user = User.objects.all()
    campos = {'id':'user_id', 'username': 'username', 'email': 'email'}
    print(request.POST)
    return render(request, 'users.html', {
        'users': user,
        'campos': campos
    })


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, user_id):
    if request.method == 'GET':
        user_info = get_object_or_404(User, pk=user_id)
        form = userForm(instance=user_info)
        return render(request, 'user_edit.html', {'user_info': user_info, 'form': form})

    else:
            user_info = get_object_or_404(User, pk=user_id)
            form = userForm(request.POST, instance=user_info)
            form.save()
            return redirect('users')


@login_required
def user_delete(request, user_id):
    user_info = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user_info.delete()
        return redirect('users')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None or user.is_active is False:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': '''<div class="alert alert-danger" role="alert">
                Try again! Username or Password incorrect. 😓 
                </div>'''
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
def management(request):
    return render(request, 'management.html')


@login_required
def vehicle(request):
    if request.method == 'POST':
        print(request.POST)
    vehiculos = vehiculo.objects.all()
    campos = [field.name for field in vehiculo._meta.get_fields()[1:]]

    return render(request, 'vehiculo.html', {
        'vehiculos': vehiculos,
        'campos': campos
    })


@login_required
def vehicle_edit(request, vehicle_id):
    if request.method == 'GET':
        vehicle_info = get_object_or_404(vehiculo, pk=vehicle_id)
        form = vehicleForm(instance=vehicle_info)
        return render(request, 'vehiculo_edit.html', {'vehicle_info': vehicle_info, 'form': form})

    else:
            vehicle_info = get_object_or_404(vehiculo, pk=vehicle_id)
            form = vehicleForm(request.POST, instance=vehicle_info)
            form.save()
            return redirect('vehiculo')


@login_required
def vehicle_delete(request, vehicle_id):
    vehicle_info = get_object_or_404(vehiculo, pk=driver_id)
    if request.method == 'POST':
        vehicle_info.delete()
        return redirect('vehiculo')


@login_required
def conductores(request):
    driver = conductor.objects.all()
    campos = [field.name for field in conductor._meta.get_fields()[1:]]

    print(request.POST)

    return render(request, 'conductor.html', {
        'drivers': driver,
        'campos': campos
    })


@login_required
def conductores_edit(request, driver_id):
    if request.method == 'GET':
        driver_info = get_object_or_404(conductor, pk=driver_id)
        form = driverForm(instance=driver_info)
        return render(request, 'conductor_edit.html', {'driver_info': driver_info, 'form': form})

    else:
            driver_info = get_object_or_404(conductor, pk=driver_id)
            form = driverForm(request.POST, instance=driver_info)
            form.save()
            return redirect('conductor')


@login_required
def conductores_delete(request, driver_id):
    driver_info = get_object_or_404(conductor, pk=driver_id)
    if request.method == 'POST':
        driver_info.delete()
        return redirect('conductor')


@login_required
def viajes(request):
    trips = viaje.objects.all()
    campos = [field.name for field in viaje._meta.get_fields()[1:]]

    return render(request, 'viajes.html', {
        'trips': trips,
        'campos': campos
    })


@login_required
def viajes_delete(request, trip_id):
    trip_info = get_object_or_404(viaje, pk=trip_id)
    if request.method == 'POST':
        trip_info.delete()
        return redirect('viajes')


@login_required
def metodos_pago(request):
    payments = metodoPago.objects.all()
    campos = [field.name for field in metodoPago._meta.get_fields()[1:]]

    return render(request, 'metodos_pago.html', {
        'payments': payments,
        'campos': campos
    })

    payments = metodoPago.objects.all()
    campos = [field.name for field in metodoPago._meta.get_fields()[1:]]

    return render(request, 'metodos_pago.html', {
        'payments': payments,
        'campos': campos
    })


@login_required
def metodos_pago_delete(request, payment_id):
    payment_info = get_object_or_404(metodoPago, pk=payment_id)
    if request.method == 'POST':
        payment_info.delete()
        return redirect('metodos_pago')
