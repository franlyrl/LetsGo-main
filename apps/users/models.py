from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    telefono = models.CharField('Teléfono', max_length=20, blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=255, blank=True, null=True)
    biografia = models.TextField('Biografía', blank=True, null=True)
    foto_perfil = models.ImageField('Foto de perfil', upload_to='perfiles/', blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username or self.email
