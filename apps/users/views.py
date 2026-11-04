from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        identifier = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Intentar autenticar por username o por email
        user = authenticate(request, username=identifier, password=password)
        if user is None:
            try:
                user_obj = Usuario.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except Usuario.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.first_name or user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'users/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        passwordr = request.POST.get('passwordr', '')

        if not email or not password:
            messages.error(request, 'Por favor completa todos los campos obligatorios.')
            return render(request, 'users/register.html')

        if password != passwordr:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'users/register.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe una cuenta registrada con este correo electrónico.')
            return render(request, 'users/register.html')

        # Generar un username único a partir del email
        base_username = email.split('@')[0]
        username = base_username
        counter = 1
        while Usuario.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=nombre
        )
        login(request, user)
        messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido {nombre or username}.')
        return redirect('home')

    return render(request, 'users/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')


@login_required
def perfil_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.telefono = request.POST.get('telefono', user.telefono)
        user.direccion = request.POST.get('direccion', user.direccion)
        user.biografia = request.POST.get('biografia', user.biografia)
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('perfil')

    return render(request, 'users/perfil.html', {'usuario': request.user})
