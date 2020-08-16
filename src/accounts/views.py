from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseNotFound

from . forms import UserRegisterForm, UserInviteForm
from . models import Invite


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


class UserInvite(View):
    form_class = UserInviteForm
    template_name = 'accounts/invite.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            invite = form.save()
            invite.save()

            domain = get_current_site(request).domain
            link = invite.get_absolute_url()

            activate_url = 'http//' + domain + link

            email_sub = 'confirm registration'
            email_body = 'please confirm your fehler account ' + activate_url

            invite.email_invite(email_sub, email_body)
            return redirect('login')

        return render(request, self.template_name, {'form': form})


class VerificationView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request, uuid):
        invite = get_object_or_404(Invite, uuid=uuid)
        if invite.is_valid() == False:
            return HttpResponseNotFound('<h1>invite not found</h1>')
        
        data = {'email': invite.email}
        form = self.form_class(initial=data)
        
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, uuid):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')

        return render(request, self.template_name, {'form': form})