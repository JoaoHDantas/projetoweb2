from django.db import models

# Create your models here.

class Interaction(models.Model):
    AVALIACAO_CHOICES = [(0, '0'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),]
    avalicao = models.PositiveSmallIntegerField(choices=AVALIACAO_CHOICES, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to='interaction-files/', blank=True, null=True)