from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
from django.contrib import messages


def home(request):
    return HttpResponse("Hello, World!")


def login_page(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account Created for {user}")
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)
