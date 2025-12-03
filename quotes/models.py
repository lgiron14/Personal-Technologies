from django.db import models
from django.utils.translation import gettext_lazy as _

class Quote(models.Model):
    """
    Representa una solicitud de cotización realizada por un cliente potencial.
    
    Almacena la información del cliente, la descripción del servicio solicitado
    y el estado de la cotización.
    """
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('sent', 'Enviada'),
        ('accepted', 'Aceptada'),
        ('rejected', 'Rechazada'),
    ]
    client_name = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    client_email = models.EmailField(verbose_name="Correo Electrónico")
    client_phone = models.CharField(max_length=20, verbose_name="Teléfono")
    description = models.TextField(verbose_name="Descripción")
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Costo Estimado")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        """Devuelve una representación legible de la cotización."""
        return f'Cotización para {self.client_name}'
