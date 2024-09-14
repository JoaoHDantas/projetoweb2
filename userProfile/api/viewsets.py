from rest_framework import viewsets
from userProfile import models
from userProfile.api import serializers

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

    