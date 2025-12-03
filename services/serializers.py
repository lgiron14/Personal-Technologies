from rest_framework import serializers
from .models import Client, Service, TechnicalReport

class ClientSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Client.
    
    Maneja la conversión de datos de clientes a JSON y viceversa.
    Incluye todos los campos del modelo.
    """
    class Meta:
        model = Client
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Service.
    
    Maneja la conversión de datos de servicios técnicos a JSON y viceversa.
    Permite la creación y actualización de servicios.
    """
    class Meta:
        model = Service
        fields = '__all__'

class TechnicalReportSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TechnicalReport.
    
    Maneja la conversión de datos de reportes técnicos a JSON y viceversa.
    Se utiliza para generar y consultar los reportes finales de los servicios.
    """
    class Meta:
        model = TechnicalReport
        fields = '__all__'
