from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from . forms import UserRegisterForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('customer')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html')


def home(request):
    return render(request, 'accounts/home.html')