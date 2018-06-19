from django.shortcuts import render, redirect, get_object_or_404
from ficha.models import Ficha
from forms import Fichaform


# Create your views here.

def ficha(request):
    form = Fichaform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'ficha.html', {'form': form})


def abrir_ficha(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    form = Fichaform(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'ler_ficha.html', {'form': form})


def apagar_ficha(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista')

    return render(request, 'apagar_ficha.html', {'paciente': paciente})

def termo(request, id):
    paciente = get_object_or_404(Ficha, pk=id)
    form = Fichaform(request.POST or None, instance=paciente)
    return render (request, 'termo.html', {'form': form})
