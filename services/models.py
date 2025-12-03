from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    """
    Representa un cliente de la empresa.
    
    Puede ser un cliente con contrato de TI o un cliente de servicio puntual.
    Almacena información de contacto y detalles de la empresa.
    """
    TYPE_CHOICES = [
        ('contract', 'Contrato TI'),
        ('punctual', 'Servicio Puntual'),
    ]
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico", unique=True)
    phone = models.CharField(max_length=20, verbose_name="Teléfono", unique=True)
    company = models.CharField(max_length=100, blank=True, verbose_name="Empresa")
    address = models.TextField(blank=True, verbose_name="Dirección")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='punctual', verbose_name="Tipo de Cliente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        """Devuelve el nombre del cliente."""
        return self.name

class Service(models.Model):
    """
    Representa un servicio técnico solicitado por un cliente.
    
    Contiene la descripción del problema, el estado del servicio
    y el técnico asignado para su resolución.
    """
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='services', verbose_name="Técnico")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    service_date = models.DateField(null=True, blank=True, verbose_name="Fecha del Servicio")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        """Devuelve el título del servicio."""
        return self.title

class TechnicalReport(models.Model):
    """
    Representa el reporte técnico final de un servicio realizado.
    
    Incluye el diagnóstico, las intervenciones realizadas, repuestos utilizados,
    recomendaciones y la firma del cliente.
    """
    service = models.OneToOneField(Service, on_delete=models.CASCADE, verbose_name="Servicio")
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Técnico")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    diagnosis = models.TextField(verbose_name="Diagnóstico")
    interventions = models.TextField(verbose_name="Intervenciones")
    parts_used = models.TextField(blank=True, verbose_name="Repuestos Utilizados")
    recommendations = models.TextField(blank=True, verbose_name="Recomendaciones")
    status = models.CharField(max_length=20, choices=[('draft', 'Borrador'), ('final', 'Final')], default='draft', verbose_name="Estado")
    signature = models.CharField(max_length=100, blank=True, verbose_name="Firma (Nombre)")
    signature_image = models.ImageField(upload_to='signatures/', null=True, blank=True, verbose_name="Imagen de Firma")
    warranty_period = models.CharField(max_length=100, blank=True, help_text="Ej: 3 meses, 1 año", verbose_name="Garantía")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Reporte Técnico"
        verbose_name_plural = "Reportes Técnicos"

    def __str__(self):
        """Devuelve una representación legible del reporte."""
        return f'Reporte para {self.service}'
