from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import TaskForm, userForm
from .models import Task

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
                return redirect('tasks')
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


@login_required
def tasks(request):
    task = Task.objects.all()

    return render(request, 'tasks.html', {
        'tasks': task
    })


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    user = User.objects.all()

    return render(request, 'users.html', {
        'users': user
    })


@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Please provide valid data'
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
def delete_user(request, user_id):
    user_info = get_object_or_404(User, pk=user_id)
    print(user_info,'-----------')
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

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': '''<div class="alert alert-danger" role="alert">
                Try again! Username or Password incorrect. 😓 
                </div>'''
            })
        else:
            login(request, user)
            return redirect('tasks')
