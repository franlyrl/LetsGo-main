from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI

# ── API Ninja ─────────────────────────────────────────────────────────────────
api = NinjaAPI(
    title="LetsGo API",
    version="1.0.0",
    description="API de la guía turística LetsGo - Puntarenas, Costa Rica"
)

from apps.transport.api import router as transport_router
from apps.services.api  import router as services_router
from apps.users.api     import router as users_router

api.add_router("/transporte/", transport_router, tags=["Transporte"])
api.add_router("/servicios/",  services_router,  tags=["Servicios"])
api.add_router("/usuarios/",   users_router,     tags=["Usuarios"])

# ── URLs principales ──────────────────────────────────────────────────────────
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('apps.core.urls')),
    path('transporte/', include('apps.transport.urls')),
    path('servicios/',  include('apps.services.urls')),
    path('usuarios/',   include('apps.users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
