from rest_framework import generics, permissions
from .models import Equipment
from .serializers import EquipmentSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Inventario'],
    summary='Listar y crear equipos',
    description='Obtiene una lista de todos los equipos en el inventario o registra uno nuevo.',
    responses={200: EquipmentSerializer(many=True), 201: EquipmentSerializer}
)
class EquipmentListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear equipos.
    
    get:
    Retorna una lista de todos los equipos.
    
    post:
    Registra un nuevo equipo en el inventario.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Inventario'],
    summary='Obtener, actualizar y eliminar equipo',
    description='Operaciones CRUD sobre un equipo específico del inventario.',
    responses={200: EquipmentSerializer, 204: None}
)
class EquipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar un equipo específico.
    
    get:
    Obtiene los detalles de un equipo.
    
    put:
    Actualiza completamente un equipo.
    
    patch:
    Actualiza parcialmente un equipo.
    
    delete:
    Elimina un equipo del inventario.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
