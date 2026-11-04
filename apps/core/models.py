from django.db import models


class Sugerencia(models.Model):
    nombre    = models.CharField(max_length=100, blank=True)
    email     = models.EmailField(blank=True)
    mensaje   = models.TextField()
    creada_en = models.DateTimeField(auto_now_add=True)
    leida     = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'
        ordering = ['-creada_en']

    def __str__(self):
        return f"Sugerencia de {self.nombre or 'Anónimo'} ({self.creada_en:%d/%m/%Y})"
