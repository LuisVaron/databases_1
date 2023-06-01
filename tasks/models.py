from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.user.username

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "task"


ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = [
    (ADDITION, _("Addition")),
    (CHANGE, _("Change")),
    (DELETION, _("Deletion")),
]

class Auditory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='timestamp')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')