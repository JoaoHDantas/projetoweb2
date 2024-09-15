from rest_framework import routers
from pixel.api.viewsets import PixelViewSet

pixel_router = routers.DefaultRouter()
pixel_router.register('pixel', PixelViewSet)