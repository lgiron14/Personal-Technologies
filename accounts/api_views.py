from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserRoleUpdateSerializer
from .models import Profile
from drf_spectacular.utils import extend_schema



class IsAdmin(permissions.BasePermission):
    """Custom permission: only allow users with Profile.role == 'admin'."""

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        try:
            return user.profile.role == 'admin'
        except Profile.DoesNotExist:
            return False


@extend_schema(tags=['Users'], summary='List all users')
class UserListAPIView(generics.ListAPIView):
    """List all users with their roles. Only accessible to admins."""

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


@extend_schema(tags=['Users'], summary='Update user role', request=UserRoleUpdateSerializer)
class UserRoleUpdateAPIView(generics.UpdateAPIView):
    """Update the role of a user. Only admins can perform this action."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        role = request.data.get('role')
        if role not in dict(Profile.ROLE_CHOICES):
            return Response({'detail': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)

        profile, created = Profile.objects.get_or_create(user=user)
        profile.role = role
        profile.save()

        return Response(self.get_serializer(user).data)
