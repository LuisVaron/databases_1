from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import *

# Register your models here.

class AuditoryAdmin(admin.ModelAdmin):

    list_display = [field.name for field in LogEntry._meta.get_fields()]

admin.site.register(LogEntry, AuditoryAdmin)

class viajesAdmin(admin.ModelAdmin):

    list_display = [field.name for field in viaje._meta.get_fields()]

admin.site.register(viaje, viajesAdmin)

