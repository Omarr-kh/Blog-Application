from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, PostCreationForm
from django.contrib import messages

from .models import Post
from django.contrib.auth.models import User


def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}

    return render(request, "home.html", context)


@login_required(login_url="login")
def create_post(request):
    user = request.user
    form = PostCreationForm()

    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(
                commit=False
            )  # Create a post instance but don't save it yet
            post.author = user  # Set the author to the logged-in user
            post.save()  # Now save the post with the user set
            return redirect("home")  # Redirect after saving

    context = {"form": form}
    return render(request, "create-post.html", context)


@login_required(login_url="login")
def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}

    return render(request, "view-post.html", context)


@login_required(login_url="login")
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.author:
        return redirect("home")

    if request.method == "POST":
        form = PostCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("view-post", post_id=post.id)

    form = PostCreationForm(instance=post)
    context = {
        "form": form,
    }
    return render(request, "create-post.html", context)


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
            messages.info(request, "Username or Password is incorrect")

    return render(request, "login.html", context)


def logout_User(request):
    logout(request)
    return redirect("home")


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
