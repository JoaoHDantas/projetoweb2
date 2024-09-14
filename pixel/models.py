from django.db import models

# Create your models here.


class Pixel(models.Model):
    descricao = models.TextField()
    upload = models.FileField(upload_to='pixels-files/', blank=True, null=True)