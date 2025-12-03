from django.urls import path
from . import views, api_views

urlpatterns = [
    # Clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/update/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    # Services
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    # Reports
    path('reports/', views.report_list, name='report_list'),
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/<int:pk>/update/', views.report_update, name='report_update'),
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('reports/<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('reports/<int:pk>/email/', views.send_report_email, name='send_report_email'),

    # API Endpoints
    path('api/clients/', api_views.ClientListCreateAPIView.as_view(), name='api-client-list'),
    path('api/clients/<int:pk>/', api_views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='api-client-detail'),
    path('api/services/', api_views.ServiceListCreateAPIView.as_view(), name='api-service-list'),
    path('api/services/<int:pk>/', api_views.ServiceRetrieveUpdateDestroyAPIView.as_view(), name='api-service-detail'),
    path('api/reports/', api_views.TechnicalReportListCreateAPIView.as_view(), name='api-report-list'),
    path('api/reports/<int:pk>/', api_views.TechnicalReportRetrieveUpdateDestroyAPIView.as_view(), name='api-report-detail'),
]