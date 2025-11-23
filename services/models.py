from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    TYPE_CHOICES = [
        ('contract', 'Contrato TI'),
        ('punctual', 'Servicio Puntual'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='punctual')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='services')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TechnicalReport(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    interventions = models.TextField()
    parts_used = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Borrador'), ('final', 'Final')], default='draft')
    signature = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Reporte para {self.service}'
