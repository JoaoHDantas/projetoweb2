from django.db import models

# Create your models here.


class Interaction(models.Model):
    comentario = models.TextField()