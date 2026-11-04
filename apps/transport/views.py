from django.shortcuts import render
from .models import Transporte


def bus_view(request):
    transportes = Transporte.objects.filter(tipo='bus', activo=True)
    return render(request, 'transport/bus.html', {'transportes': transportes})


def taxis_view(request):
    transportes = Transporte.objects.filter(tipo='taxi', activo=True)
    return render(request, 'transport/taxis.html', {'transportes': transportes})


def tren_view(request):
    transportes = Transporte.objects.filter(tipo='tren', activo=True)
    return render(request, 'transport/tren.html', {'transportes': transportes})


def maritimo_view(request):
    transportes = Transporte.objects.filter(tipo='maritimo', activo=True)
    return render(request, 'transport/maritimo.html', {'transportes': transportes})


def aereo_view(request):
    transportes = Transporte.objects.filter(tipo='aereo', activo=True)
    return render(request, 'transport/aereo.html', {'transportes': transportes})
