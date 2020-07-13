from django.forms import ModelForm
from . models import Profile, Organistion

class OrgCreationForm(ModelForm):
    class Meta:
        model = Organistion
        fields = ['name']