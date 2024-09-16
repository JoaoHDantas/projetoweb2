from django.db import models
from django.utils import timezone
# Create your models here.


class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now(), is_active=False);

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True, is_active=True)
    
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(editable=False, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(editable=False, default=True)

    objects = BaseManager()

    def delete(self, **kwargs):
        self.is_active=False
        self.deleted_at=timezone.now()
        self.save()

    def hard_delete(self, **kwargs):
        super(BaseModel, self).delete(**kwargs)

class Interaction(BaseModel):
    AVALIACAO_CHOICES = [(0, '0'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),]
    avaliacao = models.IntegerField(choices=AVALIACAO_CHOICES, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to='interaction-files/', blank=True, null=True)