from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.
def landing_view(request:HttpRequest)->HttpResponse:
    return render (request, "landing.html")