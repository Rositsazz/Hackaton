from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from .models import Recipe, User


def index(request):
    # user = User.objects.all()
    return render(request, 'index.html')
