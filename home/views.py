from django.shortcuts import render
from ficha.models import Ficha
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'registration/login.html')

@login_required
def lista(request):
    pacientes = Ficha.objects.all()
    return render(request, 'lista.html', {'pacientes': pacientes})