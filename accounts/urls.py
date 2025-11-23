from django.urls import path
from . import api_views

app_name = 'accounts'

urlpatterns = [
    path('api/users/', api_views.UserListAPIView.as_view(), name='api-user-list'),
    path('api/users/<int:pk>/role/', api_views.UserRoleUpdateAPIView.as_view(), name='api-user-role-update'),
]
