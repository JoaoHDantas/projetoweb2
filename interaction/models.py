from django.db import models

# Create your models here.


class Interaction(models.Model):
    comentario = models.TextField()
    upload = models.FileField(upload_to='interaction-files/', blank=True, null=True)