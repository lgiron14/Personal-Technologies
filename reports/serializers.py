from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Report.
    
    Maneja la conversión de datos de reportes generales a JSON y viceversa.
    """
    class Meta:
        model = Report
        fields = '__all__'
