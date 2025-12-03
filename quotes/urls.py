from django.urls import path
from . import api_views

urlpatterns = [
    path('api/quotes/', api_views.QuoteListCreateAPIView.as_view(), name='api-quote-list'),
    path('api/quotes/<int:pk>/', api_views.QuoteRetrieveUpdateDestroyAPIView.as_view(), name='api-quote-detail'),
]
