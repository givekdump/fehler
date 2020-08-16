from django.forms import ModelForm
from . models import Organistion

class OrgCreationForm(ModelForm):
    class Meta:
        model = Organistion
        fields = ['name']