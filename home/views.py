from django.shortcuts import render
from ficha.models import Ficha
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'registration/login.html')

@login_required
def lista(request):
    pacientes = Ficha.objects.filter(user=request.user)
    return render(request, 'lista.html', {'pacientes': pacientes})