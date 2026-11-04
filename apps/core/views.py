from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sugerencia
from apps.services.models import ServicioTuristico
from apps.transport.models import Transporte


def home(request):
    if request.method == 'POST':
        texto = request.POST.get('sugerencias', '').strip()
        if texto:
            Sugerencia.objects.create(mensaje=texto)
            messages.success(request, '¡Muchas gracias por tu sugerencia!')
            return redirect('home')

    servicios_destacados = ServicioTuristico.objects.filter(activo=True, destacado=True)[:6]
    transportes_principales = Transporte.objects.filter(activo=True)[:4]

    return render(request, 'core/index.html', {
        'servicios_destacados': servicios_destacados,
        'transportes_principales': transportes_principales,
    })


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()

        if mensaje:
            Sugerencia.objects.create(nombre=nombre, email=email, mensaje=mensaje)
            messages.success(request, '¡Gracias por comunicarte con nosotros! Te responderemos pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor escribe un mensaje antes de enviar.')

    return render(request, 'core/contacto.html')


def recomendaciones(request):
    return render(request, 'core/recomendaciones.html')


def recursos_adicionales(request):
    return render(request, 'core/recursosAdicionales.html')
