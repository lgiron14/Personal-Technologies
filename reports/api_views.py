from rest_framework import generics, permissions
from .models import Report
from .serializers import ReportSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Reportes Generales'],
    summary='Listar y crear reportes generales',
    description='Obtiene una lista de todos los reportes generales o crea uno nuevo.',
    responses={200: ReportSerializer(many=True), 201: ReportSerializer}
)
class ReportListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear reportes generales.
    
    get:
    Retorna una lista de todos los reportes.
    
    post:
    Crea un nuevo reporte general.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Reportes Generales'],
    summary='Obtener, actualizar y eliminar reporte general',
    description='Operaciones CRUD sobre un reporte general específico.',
    responses={200: ReportSerializer, 204: None}
)
class ReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar un reporte general específico.
    
    get:
    Obtiene los detalles de un reporte.
    
    put:
    Actualiza completamente un reporte.
    
    patch:
    Actualiza parcialmente un reporte.
    
    delete:
    Elimina un reporte.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
