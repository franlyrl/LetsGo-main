from django.db import models


class ServicioTuristico(models.Model):
    CATEGORIA_CHOICES = [
        ('rentacar', 'Alquiler de Vehículos / Rent a Car'),
        ('acuatico', 'Deporte Acuático y Recreación'),
        ('hospedaje', 'Hospedaje'),
        ('tour', 'Tours y Excursiones'),
    ]

    nombre = models.CharField('Nombre del Servicio o Empresa', max_length=150)
    categoria = models.CharField('Categoría', max_length=20, choices=CATEGORIA_CHOICES, db_index=True)
    descripcion = models.TextField('Descripción')
    ubicacion = models.CharField('Ubicación / Dirección', max_length=200, blank=True)
    precio_desde = models.CharField('Precio desde', max_length=80, blank=True)
    telefono = models.CharField('Teléfono', max_length=30, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=30, blank=True)
    email = models.EmailField('Email de Contacto', blank=True)
    sitio_web = models.URLField('Sitio Web o Redes', blank=True)
    imagen = models.ImageField('Imagen', upload_to='servicios/', blank=True, null=True)
    destacado = models.BooleanField('Destacado en portada', default=False)
    activo = models.BooleanField('Activo', default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio Turístico'
        verbose_name_plural = 'Servicios Turísticos'
        ordering = ['categoria', '-destacado', 'nombre']

    def __str__(self):
        return f"[{self.get_categoria_display()}] {self.nombre}"
