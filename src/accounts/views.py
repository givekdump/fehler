from django.shortcuts import render, redirect
from . forms import UserRegisterForm


def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})