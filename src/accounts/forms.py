from django.contrib.auth.forms import UserCreationForm
from django import forms

from . models import User, Invite

#from customers.models import Organistion

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1', 'password2', 'first_name', 'last_name']


class UserInviteForm(forms.ModelForm):

    class Meta:
        model = Invite
        fields = ['email']