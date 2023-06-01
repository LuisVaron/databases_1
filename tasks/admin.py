from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Task
from .models import Auditory

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("createdAt", )

class AuditoryAdmin(admin.ModelAdmin):

    list_display = [field.name for field in LogEntry._meta.get_fields()]

admin.site.register(Task, TaskAdmin)
admin.site.register(LogEntry, AuditoryAdmin)
