from django.urls import path
from . import views

urlpatterns = [
    path('rentacar/',  views.rentacar_view,  name='servicios_rentacar'),
    path('acuatico/',  views.acuatico_view,  name='servicios_acuatico'),
    path('hospedaje/', views.hospedaje_view, name='servicios_hospedaje'),
    path('tours/',     views.tours_view,     name='servicios_tours'),
]
