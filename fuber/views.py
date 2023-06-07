from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
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
def signout(request):
    logout(request)
    return redirect('home')


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    if request.method == 'GET':
        user = User.objects.all()
        txtFilter = ''
    else:
        kwargs = {request.POST['field'] + '__contains': request.POST['txtFilter']}
        user = User.objects.filter(**kwargs)
        txtFilter = request.POST['txtFilter']

    campos = ['id', 'username', 'email']
    return render(request, 'users.html', {
        'users': user,
        'campos': campos,
        'txtFilter': txtFilter
    })


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, user_id):
    user_info = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        user_info = get_object_or_404(User, pk=user_id)
        form = userForm(instance=user_info)
        return render(request, 'user_edit.html', {'user_info': user_info, 'form': form})

    else:
        form = userForm(request.POST, instance=user_info)
        print(form.errors)
        form.save()
        return redirect('users')


@login_required
def user_delete(request, user_id):
    user_info = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user_info.delete()
        return redirect('users')


@login_required
def user_create(request,):
    if request.method == 'GET':
        return render(request, 'user_create.html', {
            'form': createUserForm
        })
    
    else:
        user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name']
                )
        user.save()
        form = createUserForm(request.POST)
        return redirect('users')


@login_required
def management(request):
    return render(request, 'management.html')


@login_required
def vehicle(request):
    if request.method == 'GET':
        vehiculos = vehiculo.objects.all()
        txtFilter = ''
    else:
        kwargs = {request.POST['field'] + '__contains': request.POST['txtFilter']}
        vehiculos = vehiculo.objects.filter(**kwargs)
        txtFilter = request.POST['txtFilter']
        
    campos = ['vehicle_id', 'marca', 'color', 'placa']

    return render(request, 'vehiculo.html', {
        'vehiculos': vehiculos,
        'campos': campos,
        'txtFilter': txtFilter
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
def vehicle_create(request,):
    if request.method == 'GET':
        return render(request, 'vehiculo_create.html', {
            'form': createVehicleForm
        })
    
    else:
        try:
            form = createVehicleForm(request.POST)
            new_vehicle = form.save(commit=False)
            new_vehicle.save()
            return redirect('vehiculo')
        except:
            return render(request, 'vehiculo_create.html', {
                'form': createVehicleForm,
                'error': '''<div class="alert alert-danger" role="alert">
                    Try again! Insert a plate that not exists already.
                    </div>'''
            })


@login_required
def conductores(request):
    if request.method == 'GET':
        driver = conductor.objects.all()
        txtFilter = ''
    else:
        if request.POST['field'] == 'placa':
            kwargs = {'vehicle__placa__contains': request.POST['txtFilter']}
        else:
            kwargs = {request.POST['field'] + '__contains': request.POST['txtFilter']}
        driver = conductor.objects.filter(**kwargs)
        txtFilter = request.POST['txtFilter']
        
    campos = ['driver_id', 'nombre', 'correo', 'placa']

    return render(request, 'conductor.html', {
        'drivers': driver,
        'campos': campos,
        'txtFilter': txtFilter
    })


@login_required
def conductores_create(request,):
    if request.method == 'GET':
        return render(request, 'conductor_create.html', {
            'form': driverForm
        })
    
    else:
        try:
            form = driverForm(request.POST)
            new_driver = form.save(commit=False)
            new_driver.save()
            return redirect('conductores')
        except:
            return render(request, 'conductor_create.html', {
                'form': driverForm,
                'error': '''<div class="alert alert-danger" role="alert">
                    Assign a vehicle that has not been assigned.
                    </div>'''
            })


@login_required
def conductores_edit(request, driver_id):
    if request.method == 'GET':
        driver_info = get_object_or_404(conductor, pk=driver_id)
        form = driverForm(instance=driver_info)
        return render(request, 'conductor_edit.html', {'driver_info': driver_info, 'form': form})

    else:
        try:
            driver_info = get_object_or_404(conductor, pk=driver_id)
            form = driverForm(request.POST, instance=driver_info)
            form.save()
            return redirect('conductores')
        except:
            return render(request, 'conductor_edit.html', {
                'driver_info': driver_info, 
                'form': form,
                'error': '''<div class="alert alert-danger" role="alert">
                The vehicle is already assigned to another driver 😓 
                </div>'''}
                )


@login_required
def conductores_delete(request, driver_id):
    driver_info = get_object_or_404(conductor, pk=driver_id)
    if request.method == 'POST':
        driver_info.delete()
        return redirect('conductor')


@login_required
def viajes(request):
    fields = {'conductor': 'driver', 'pasajero': 'user', 'origen': 'direccion_origen', 'destino':'direccion_destino'}
    if request.method == 'GET':
        trips = viaje.objects.all()
        txtFilter = ''
    else:
        if fields[request.POST['field']] == 'driver':
            kwargs = {'driver__nombre__contains': request.POST['txtFilter']}
        elif fields[request.POST['field']] =='user':
            kwargs = {'user__first_name__contains': request.POST['txtFilter']}
        else:
            kwargs = {fields[request.POST['field']] + '__contains': request.POST['txtFilter']}
        trips = viaje.objects.filter(**kwargs)
        txtFilter = request.POST['txtFilter']

    campos = ['conductor', 'pasajero', 'origen', 'destino']
    return render(request, 'viajes.html', {
        'trips': trips,
        'campos': campos,
        'txtFilter': txtFilter
    })


@login_required
def viajes_create(request,):
    if request.method == 'GET':
        return render(request, 'viajes_create.html', {
            'form': tripForm
        })
    
    else:
        try:
            form = tripForm(request.POST)
            new_trip = form.save(commit=False)
            new_trip.save()
            return redirect('viajes')
        except:
            return render(request, 'viajes_create.html', {
                'form': createVehicleForm,
                'error': '''<div class="alert alert-danger" role="alert">
                    Try again! Validate the information.
                    </div>'''
            })


@login_required
def viajes_edit(request, trip_id):
    if request.method == 'GET':
        trip_info = get_object_or_404(viaje, pk=trip_id)
        form = tripForm(instance=trip_info)
        return render(request, 'viajes_edit.html', {'trip_info': trip_info, 'form': form})

    else:
            trip_info = get_object_or_404(viaje, pk=trip_id)
            form = tripForm(request.POST, instance=trip_info)
            form.save()
            return redirect('viajes')


@login_required
def viajes_delete(request, trip_id):
    trip_info = get_object_or_404(viaje, pk=trip_id)
    if request.method == 'POST':
        trip_info.delete()
        return redirect('viajes')


@login_required
def metodos_pago(request):
    if request.method == 'GET':
        payments = metodoPago.objects.all()
        txtFilter = ''
    else:
        kwargs = {request.POST['field'] + '__contains': request.POST['txtFilter']}
        payments = metodoPago.objects.filter(**kwargs)
        txtFilter = request.POST['txtFilter']
        
    campos = ['payment_id', 'marca', 'tipo']

    return render(request, 'metodos_pago.html', {
        'payments': payments,
        'campos': campos,
        'txtFilter': txtFilter
    })

    payments = metodoPago.objects.all()
    campos = [field.name for field in metodoPago._meta.get_fields()[1:]]

    return render(request, 'metodos_pago.html', {
        'payments': payments,
        'campos': campos
    })


@login_required
def metodos_pago_create(request,):
    if request.method == 'GET':
        return render(request, 'metodos_pago_create.html', {
            'form': paymentForm
        })
    
    else:
        try:
            form = paymentForm(request.POST)
            new_payment = form.save(commit=False)
            new_payment.save()
            return redirect('metodos_pago')
        except:
            return render(request, 'metodos_pago_create.html', {
                'form': createVehicleForm,
                'error': '''<div class="alert alert-danger" role="alert">
                    Try again! Validate the information.
                    </div>'''
            })


@login_required
def metodos_pago_edit(request, payment_id):
    if request.method == 'GET':
        payment_info = get_object_or_404(metodoPago, pk=payment_id)
        form = paymentForm(instance=payment_info)
        return render(request, 'metodos_pago_edit.html', {'payment_info': payment_info, 'form': form})

    else:
            payment_info = get_object_or_404(metodoPago, pk=payment_id)
            form = paymentForm(request.POST, instance=payment_info)
            form.save()
            return redirect('metodos_pago')


@login_required
def metodos_pago_delete(request, payment_id):
    payment_info = get_object_or_404(metodoPago, pk=payment_id)
    if request.method == 'POST':
        payment_info.delete()
        return redirect('metodos_pago')
    