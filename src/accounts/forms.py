from django.contrib.auth.forms import UserCreationForm
from . models import User
from customers.models import Organistion

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1', 'password2', 'first_name', 'last_name']