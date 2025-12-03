from django.contrib import admin
from .models import Client, Service, TechnicalReport

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Client.
    """
    list_display = ('name', 'email', 'phone', 'company', 'type', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'company')
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Service.
    """
    list_display = ('title', 'client', 'technician', 'status', 'service_date', 'created_at')
    list_filter = ('status', 'service_date', 'created_at')
    search_fields = ('title', 'description', 'client__name', 'technician__username')
    date_hierarchy = 'service_date'
    ordering = ('-created_at',)
    autocomplete_fields = ['client']

@admin.register(TechnicalReport)
class TechnicalReportAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo TechnicalReport.
    """
    list_display = ('service', 'technician', 'date', 'status', 'warranty_period')
    list_filter = ('status', 'date')
    search_fields = ('service__title', 'technician__username', 'diagnosis')
    date_hierarchy = 'date'
    ordering = ('-date',)
