from rest_framework import serializers
from pixel.models import Pixel

class PixelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pixel
        fields = '__all__'