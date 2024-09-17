from rest_framework import viewsets, permissions
from userProfile import models
from userProfile.api import serializers
from .permissions import IsInSpecificGroup
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]

    