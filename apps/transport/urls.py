from django.urls import path
from . import views

urlpatterns = [
    path('bus/',      views.bus_view,      name='transporte_bus'),
    path('taxis/',    views.taxis_view,    name='transporte_taxis'),
    path('tren/',     views.tren_view,     name='transporte_tren'),
    path('maritimo/', views.maritimo_view, name='transporte_maritimo'),
    path('aereo/',    views.aereo_view,    name='transporte_aereo'),
]
