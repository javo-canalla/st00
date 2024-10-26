from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, CustomUserCreationForm, CustomPasswordResetForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from .decorators import admin_required
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
# from django.contrib.auth.models import auth

# Create your views here.

CustomUser = get_user_model()


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


@admin_required(login_url='access_denied')
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
            messages.error(request, 'Por favor corrige los errores abajo.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'userapp/change_password.html', context)


def logout(request):
    auth_logout(request)
    return redirect("homepage")


def access_denied(request):
    return render(request, 'userapp/access_denied.html')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'userapp/password_reset_form.html'
    email_template_name = 'userapp/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = CustomPasswordResetForm
    subject_template_name = 'userapp/password_reset_subject.txt'
    extra_email_context = {
        'protocol': 'http',
        'domain': 'localhost:8000',
    }


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'userapp/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'userapp/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'userapp/password_reset_complete.html'


@admin_required(login_url='login')
def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'userapp/user_list.html', context)


@admin_required(login_url='login')
def user_edit(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    context = {'form': form, 'user': user}
    return render(request, 'userapp/user_edit.html', context)

# def new_job(request):
#     return HttpResponse("new job")

# def list_job(request):
#     return HttpResponse("list jobs")
