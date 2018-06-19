from django.shortcuts import render
from ficha.models import Ficha
# Create your views here.

def home(request):
    return render(request, 'home.html')

def lista(request):
    pacientes = Ficha.objects.all()
    return render(request, 'lista.html', {'pacientes': pacientes})