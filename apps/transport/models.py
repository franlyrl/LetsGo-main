from django.db import models


class Transporte(models.Model):
    TIPO_CHOICES = [
        ('bus', 'Autobús'),
        ('taxi', 'Taxi'),
        ('tren', 'Tren'),
        ('maritimo', 'Transporte Marítimo / Ferry'),
        ('aereo', 'Transporte Aéreo'),
    ]

    nombre = models.CharField('Nombre / Servicio', max_length=150)
    tipo = models.CharField('Tipo de Transporte', max_length=20, choices=TIPO_CHOICES, db_index=True)
    descripcion = models.TextField('Descripción')
    origen = models.CharField('Punto de Origen', max_length=120, blank=True)
    destino = models.CharField('Destino', max_length=120, blank=True)
    horario = models.CharField('Horarios de Salida', max_length=200, blank=True)
    tarifa = models.CharField('Tarifa Estimada', max_length=80, blank=True)
    empresa = models.CharField('Empresa u Operador', max_length=120, blank=True)
    telefono = models.CharField('Teléfono', max_length=30, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=30, blank=True)
    sitio_web = models.URLField('Sitio Web', blank=True)
    imagen = models.ImageField('Imagen', upload_to='transporte/', blank=True, null=True)
    activo = models.BooleanField('Activo', default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Medio de Transporte'
        verbose_name_plural = 'Medios de Transporte'
        ordering = ['tipo', 'nombre']

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.nombre}"
