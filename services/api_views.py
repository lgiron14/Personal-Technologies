from rest_framework import generics, permissions
from .models import Client, Service, TechnicalReport
from .serializers import ClientSerializer, ServiceSerializer, TechnicalReportSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

# Client Views
@extend_schema(
    tags=['Clientes'],
    summary='Listar y crear clientes',
    description='Obtiene una lista de todos los clientes registrados o crea uno nuevo. Requiere autenticación.',
    responses={200: ClientSerializer(many=True), 201: ClientSerializer}
)
class ClientListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear clientes.
    
    get:
    Retorna una lista de todos los clientes existentes.
    
    post:
    Crea una nueva instancia de cliente.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Clientes'],
    summary='Obtener, actualizar y eliminar cliente',
    description='Operaciones CRUD sobre un cliente específico identificado por su ID.',
    responses={200: ClientSerializer, 204: None}
)
class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar un cliente específico.
    
    get:
    Obtiene los detalles de un cliente.
    
    put:
    Actualiza completamente un cliente.
    
    patch:
    Actualiza parcialmente un cliente.
    
    delete:
    Elimina un cliente.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

# Service Views
@extend_schema(
    tags=['Servicios'],
    summary='Listar y crear servicios',
    description='Obtiene una lista de todos los servicios técnicos o crea uno nuevo.',
    responses={200: ServiceSerializer(many=True), 201: ServiceSerializer}
)
class ServiceListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear servicios técnicos.
    
    get:
    Retorna una lista de todos los servicios.
    
    post:
    Crea un nuevo servicio técnico.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Servicios'],
    summary='Obtener, actualizar y eliminar servicio',
    description='Operaciones CRUD sobre un servicio técnico específico.',
    responses={200: ServiceSerializer, 204: None}
)
class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar un servicio específico.
    
    get:
    Obtiene los detalles de un servicio.
    
    put:
    Actualiza completamente un servicio.
    
    patch:
    Actualiza parcialmente un servicio.
    
    delete:
    Elimina un servicio.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Technical Report Views
@extend_schema(
    tags=['Reportes Técnicos'],
    summary='Listar y crear reportes',
    description='Obtiene una lista de reportes técnicos o crea uno nuevo.',
    responses={200: TechnicalReportSerializer(many=True), 201: TechnicalReportSerializer}
)
class TechnicalReportListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear reportes técnicos.
    
    get:
    Retorna una lista de todos los reportes.
    
    post:
    Crea un nuevo reporte técnico.
    """
    queryset = TechnicalReport.objects.all()
    serializer_class = TechnicalReportSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    tags=['Reportes Técnicos'],
    summary='Obtener, actualizar y eliminar reporte',
    description='Operaciones CRUD sobre un reporte técnico específico.',
    responses={200: TechnicalReportSerializer, 204: None}
)
class TechnicalReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de API para gestionar un reporte técnico específico.
    
    get:
    Obtiene los detalles de un reporte.
    
    put:
    Actualiza completamente un reporte.
    
    patch:
    Actualiza parcialmente un reporte.
    
    delete:
    Elimina un reporte.
    """
    queryset = TechnicalReport.objects.all()
    serializer_class = TechnicalReportSerializer
    permission_classes = [permissions.IsAuthenticated]
