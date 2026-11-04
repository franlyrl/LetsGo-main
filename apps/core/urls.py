from django.urls import path
from . import views

urlpatterns = [
    path('',                views.home,                 name='home'),
    path('contacto/',       views.contacto,             name='contacto'),
    path('recomendaciones/', views.recomendaciones,     name='recomendaciones'),
    path('recursos/',       views.recursos_adicionales, name='recursos'),
]
