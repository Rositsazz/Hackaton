from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from .models import Recipe, User


def index(request):
    if request.user.is_authenticated():
        return redirect("logged.html")   # todo logged.hmtl

    if request.method == "POST":
        print("hellloouuuuu")
    else:
        return render(request, 'index.html', locals())


def _validate_register(username, email, password):
    if username is None or username.strip() == "":
        return False

    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "":
        return False

    return True


def register(request):
    if request.user.is_authenticated():
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not _validate_register(username, email, password):
            return HttpResponseBadRequest("Something is missing")

        user = User.objects.create_user(username, email, password)
        return redirect('signin')

    else:
        return render(request, 'register.html', locals())


def signin(request):
    if request.user.is_authenticated():
        return redirect("logged")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("logged")
        else:
            return redirect("signin")

    else:
        return render(request, "login.html", locals())


def logged(request):
    return render(request, "logged.html")


def dummy(request):
    return render(request, "dummy.html")
