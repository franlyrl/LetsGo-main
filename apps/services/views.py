from django.shortcuts import render
from .models import ServicioTuristico


def rentacar_view(request):
    servicios = ServicioTuristico.objects.filter(categoria='rentacar', activo=True)
    return render(request, 'services/rentacar.html', {'servicios': servicios})


def acuatico_view(request):
    servicios = ServicioTuristico.objects.filter(categoria='acuatico', activo=True)
    return render(request, 'services/alquilerAcuatico.html', {'servicios': servicios})


def hospedaje_view(request):
    servicios = ServicioTuristico.objects.filter(categoria='hospedaje', activo=True)
    return render(request, 'services/hospedaje.html', {'servicios': servicios})


def tours_view(request):
    servicios = ServicioTuristico.objects.filter(categoria='tour', activo=True)
    return render(request, 'services/tour.html', {'servicios': servicios})
