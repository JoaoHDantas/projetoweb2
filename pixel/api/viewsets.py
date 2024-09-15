from rest_framework import viewsets
from pixel.models import Pixel
from pixel.api.serializers import PixelSerializer

class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer