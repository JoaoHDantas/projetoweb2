from rest_framework import routers
from userProfile.api import viewsets


userProfile_router = routers.DefaultRouter()
userProfile_router.register('userProfile', viewsets.UserProfileViewSet)