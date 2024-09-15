from django.db import models

# Create your models here.


class Pixel(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to='pixels-files/', blank=True, null=True)