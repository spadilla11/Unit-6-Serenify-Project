from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.conf import settings
from django.contrib.auth.decorators import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
# import random



# Create your views here.
def landing_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'landing.html')


def register_view(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserStats.objects.create(user=user)
                login(request, user)
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def login_view(request:HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request:HttpRequest)->HttpResponse:
    logout(request)
    return redirect('landing')


def user_stats(request:HttpRequest)->HttpResponse:
    pass

def profile_view(request: HttpRequest) -> HttpResponse:
    # userstats = UserStats.objects.get_or_create(user = request.user)
    stats = request.user.userstats
    name = request.user.username
    return render(request, 'profile.html', {'name':name, 'stats' : stats})

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')