from ninja import Router, Schema
from typing import List, Optional
from .models import Transporte

router = Router()


class TransporteOut(Schema):
    id: int
    nombre: str
    tipo: str
    descripcion: str
    origen: Optional[str] = ""
    destino: Optional[str] = ""
    horario: Optional[str] = ""
    tarifa: Optional[str] = ""
    empresa: Optional[str] = ""
    telefono: Optional[str] = ""
    whatsapp: Optional[str] = ""
    sitio_web: Optional[str] = ""


@router.get("/", response=List[TransporteOut])
def list_transportes(request, tipo: Optional[str] = None):
    qs = Transporte.objects.filter(activo=True)
    if tipo:
        qs = qs.filter(tipo=tipo)
    return list(qs)


@router.get("/{transporte_id}", response={200: TransporteOut, 404: dict})
def get_transporte(request, transporte_id: int):
    try:
        return 200, Transporte.objects.get(id=transporte_id, activo=True)
    except Transporte.DoesNotExist:
        return 404, {"message": "Transporte no encontrado"}
