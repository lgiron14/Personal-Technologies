from rest_framework import serializers
from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Equipment.
    
    Maneja la conversión de datos de equipos de inventario a JSON y viceversa.
    """
    class Meta:
        model = Equipment
        fields = '__all__'
