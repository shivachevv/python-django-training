from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def login_controller(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


def register_controller(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def logout_controller(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
