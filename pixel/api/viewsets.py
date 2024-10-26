from rest_framework import viewsets, permissions
from pixel.models import Pixel
from pixel.api.serializers import PixelSerializer
from .permissions import IsInSpecificGroup
# CanViewPostsGroup

class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]