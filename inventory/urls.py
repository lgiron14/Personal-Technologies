from django.urls import path
from . import api_views

urlpatterns = [
    path('api/equipment/', api_views.EquipmentListCreateAPIView.as_view(), name='api-equipment-list'),
    path('api/equipment/<int:pk>/', api_views.EquipmentRetrieveUpdateDestroyAPIView.as_view(), name='api-equipment-detail'),
]
