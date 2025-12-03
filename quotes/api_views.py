from rest_framework import generics, permissions
from .models import Quote
from .serializers import QuoteSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Cotizaciones'],
    summary='Listar y crear cotizaciones',
    description='Obtiene una lista de todas las cotizaciones o registra una nueva solicitud.',
    responses={200: QuoteSerializer(many=True), 201: QuoteSerializer}
)
class QuoteListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear cotizaciones.
    
    get:
    Retorna una lista de todas las cotizaciones.
    
    post:
    Crea una nueva solicitud de cotización.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Cotizaciones'],
    summary='Obtener, actualizar y eliminar cotización',
    description='Operaciones CRUD sobre una cotización específica.',
    responses={200: QuoteSerializer, 204: None}
)
class QuoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar una cotización específica.
    
    get:
    Obtiene los detalles de una cotización.
    
    put:
    Actualiza completamente una cotización.
    
    patch:
    Actualiza parcialmente una cotización.
    
    delete:
    Elimina una cotización.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]
