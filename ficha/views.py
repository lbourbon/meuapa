from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ficha.models import Ficha
from forms import Fichaform


# Create your views here.
@login_required
def ficha(request):
    form = Fichaform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'ficha.html', {'form': form})

@login_required
def abrir_ficha(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    form = Fichaform(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'ler_ficha.html', {'form': form})

@login_required
def apagar_ficha(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista')

    return render(request, 'apagar_ficha.html', {'paciente': paciente})

@login_required
def termo(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    form = Fichaform(request.POST or None, instance=paciente)
    return render (request, 'termo.html', {'form': form})
