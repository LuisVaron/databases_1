from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class userForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
