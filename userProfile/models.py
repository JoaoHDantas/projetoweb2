from django.db import models
from pixel.models import Pixel

# Create your models here.


class UserProfile(models.Model):
    fraseEfeito = models.TextField()
    profile_picture = models.ImageField(upload_to='profile-images/', blank=True, null=True)
    userPixels = models.ForeignKey(Pixel, on_delete = models.CASCADE, blank=True, null=True)
    # fotoPerfil = models.ImageField()