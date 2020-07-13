from django.shortcuts import render, redirect
from . forms import OrgCreationForm
from . models import Organistion
# Create your views here.


def orgRegister(request):
    if request.method == 'POST':
        form = OrgCreationForm(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            org.owner = request.user
            org.name = form.cleaned_data['name']
            org.save()
            return redirect('index')
    else:
        form = OrgCreationForm()
    return render(request, 'customers/org.html', {'form': form})
