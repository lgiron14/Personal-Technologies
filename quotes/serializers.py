from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Quote.
    
    Maneja la conversión de datos de cotizaciones a JSON y viceversa.
    """
    class Meta:
        model = Quote
        fields = '__all__'
