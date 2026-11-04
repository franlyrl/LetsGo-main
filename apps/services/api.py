from ninja import Router, Schema
from typing import List, Optional
from .models import ServicioTuristico

router = Router()


class ServicioOut(Schema):
    id: int
    nombre: str
    categoria: str
    descripcion: str
    ubicacion: Optional[str] = ""
    precio_desde: Optional[str] = ""
    telefono: Optional[str] = ""
    whatsapp: Optional[str] = ""
    email: Optional[str] = ""
    sitio_web: Optional[str] = ""
    destacado: bool = False


@router.get("/", response=List[ServicioOut])
def list_servicios(request, categoria: Optional[str] = None):
    qs = ServicioTuristico.objects.filter(activo=True)
    if categoria:
        qs = qs.filter(categoria=categoria)
    return list(qs)


@router.get("/{servicio_id}", response={200: ServicioOut, 404: dict})
def get_servicio(request, servicio_id: int):
    try:
        return 200, ServicioTuristico.objects.get(id=servicio_id, activo=True)
    except ServicioTuristico.DoesNotExist:
        return 404, {"message": "Servicio no encontrado"}
