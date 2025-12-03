from django.db import models

class Equipment(models.Model):
    """
    Representa un equipo o dispositivo en el inventario de la empresa.
    
    Permite realizar un seguimiento del estado, ubicación y detalles de compra
    de cada activo tecnológico.
    """
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('in_use', 'En Uso'),
        ('maintenance', 'En Mantenimiento'),
        ('damaged', 'Dañado'),
    ]
    model = models.CharField(max_length=100, verbose_name="Modelo")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Número de Serie")
    description = models.TextField(blank=True, verbose_name="Descripción")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Estado")
    location = models.CharField(max_length=100, blank=True, verbose_name="Ubicación")
    purchase_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Compra")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        """Devuelve una representación legible del equipo."""
        return f'{self.model} - {self.serial_number}'
