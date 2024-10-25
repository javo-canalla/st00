from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .decorators import admin_required
# from django.contrib.auth.models import auth

# Create your views here.


def homepage(request):
    return render(request, 'userapp/index.html')


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("dashboard")
    context = {'loginform': form}
    return render(request, 'userapp/login.html', context)


@admin_required(login_url='login')
def register(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'userapp/register.html', context)


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'userapp/dashboard.html')


@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Actualizamos la sesión para que el usuario no sea deslogueado
            update_session_auth_hash(request, user)
            return redirect('dashboard')
        else:
            # Opcional: Puedes agregar un mensaje de error aquí
            pass
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'userapp/change_password.html', context)


def forgot_password(request):
    return HttpResponse("forgot password")


def logout(request):
    auth_logout(request)
    return redirect("")

# def new_job(request):
#     return HttpResponse("new job")

# def list_job(request):
#     return HttpResponse("list jobs")
