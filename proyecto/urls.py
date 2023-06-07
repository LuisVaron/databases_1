"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fuber import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='sigin'),
    path('users/', views.users, name='users'),
    path('users/create', views.user_create, name='user_create'),
    path('users/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete', views.user_delete, name='user_delete'),
    path('management/', views.management, name='management'),
    path('conductores/', views.conductores, name='conductores'),
    path('conductores/create', views.conductores_create, name='conductores_create'),
    path('conductores/<int:driver_id>/', views.conductores_edit, name='conductores_edit'),
    path('conductores/<int:trip_id>/delete', views.conductores_delete, name='conductores_delete'),
    path('vehiculo/', views.vehicle, name='vehiculo'),
    path('vehiculo/create', views.vehicle_create, name='vehiculo_create'),
    path('vehiculo/<int:vehicle_id>/', views.vehicle_edit, name='vehicle_edit'),
    path('vehiculo/<int:trip_id>/delete', views.vehicle_delete, name='vehiculo_delete'),
    path('viajes/', views.viajes, name='viajes'),
    path('viajes/create', views.viajes_create, name='viajes_create'),
    path('viajes/<int:trip_id>/', views.viajes_edit, name='viajes_edit'),
    path('viajes/<int:trip_id>/delete', views.viajes_delete, name='viajes_delete'),
    path('metodos_pago/', views.metodos_pago, name='metodos_pago'),
    path('metodos_pago/create', views.metodos_pago_create, name='metodos_pago_create'),
    path('metodos_pago/<int:payment_id>/', views.metodos_pago_edit, name='metodos_pago_edit'),
    path('metodos_pago/<int:payment_id>/delete', views.metodos_pago_delete, name='metodos_pago_delete'),
]
