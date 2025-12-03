from django.urls import path
from . import api_views

urlpatterns = [
    path('api/general-reports/', api_views.ReportListCreateAPIView.as_view(), name='api-general-report-list'),
    path('api/general-reports/<int:pk>/', api_views.ReportRetrieveUpdateDestroyAPIView.as_view(), name='api-general-report-detail'),
]
