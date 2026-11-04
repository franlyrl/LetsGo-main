from ninja import Router, Schema
from typing import Optional, List
from django.contrib.auth import authenticate
from .models import Usuario

router = Router()


class UserOut(Schema):
    id: int
    username: str
    email: str
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    telefono: Optional[str] = None
    direccion: Optional[str] = None


class UserRegisterIn(Schema):
    nombre: str
    email: str
    password: str
    telefono: Optional[str] = None


@router.get("/me", response={200: UserOut, 401: dict})
def get_current_user(request):
    if not request.user.is_authenticated:
        return 401, {"message": "No autenticado"}
    return request.user


@router.post("/registro", response={201: UserOut, 400: dict})
def api_register_user(request, payload: UserRegisterIn):
    if Usuario.objects.filter(email=payload.email).exists():
        return 400, {"message": "El correo ya está registrado"}

    base_username = payload.email.split('@')[0]
    username = base_username
    counter = 1
    while Usuario.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1

    user = Usuario.objects.create_user(
        username=username,
        email=payload.email,
        password=payload.password,
        first_name=payload.nombre,
        telefono=payload.telefono
    )
    return 201, user


@router.get("/lista", response=List[UserOut])
def list_users(request):
    # Retorna lista básica de usuarios activos
    return Usuario.objects.filter(is_active=True)[:20]
