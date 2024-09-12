from django.db import models

# Create your models here.


class UserProfile(models.Model):
    fraseEfeito = models.TextField()

    # fotoPerfil = models.ImageField()