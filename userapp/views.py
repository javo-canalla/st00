from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

# Create your views here.
def homepage(request):
    return render(request, 'userapp/index.html')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'loginform': form}
    return render(request, 'userapp/login.html', context=context)

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'userapp/dashboard.html')

def pass_change(request):
    return HttpResponse("password change")

def logout(request):
    auth.logout(request)
    return redirect("")

# def new_job(request):
#     return HttpResponse("new job")

# def list_job(request):
#     return HttpResponse("list jobs")