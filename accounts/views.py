from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    context = {'form': UserCreationForm()}
    error = {'form': UserCreationForm(), 'Error': 'User already exists.'}
    pass_error = {'form': UserCreationForm(), 'Error': 'Passwords does not match.'}
    if request.method == 'GET':
        return render(request, 'register.html', context)
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            #return render(request, 'home.html')
            return redirect('login')
        except IntegrityError:
            #if user already exists.
            return render(request, 'register.html', error)
    else:
        return render(request, 'register.html', pass_error)

def loginuser(request):
    context = {'form': AuthenticationForm(), 'Error': 'Please login.'}
    error= {'form': AuthenticationForm(), 'Error':'Username/Password is invalid.'}
    if request.method == 'GET':
        return render(request, 'login.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', error)
        else:
            login(request, user)
            return render(request, 'home.html')

@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')