from django.db import models
from pixel.models import Pixel
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
class UserProfile(BaseModel):
    fraseEfeito = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile-images/', blank=True, null=True)
    userPixels = models.ForeignKey(Pixel, on_delete = models.CASCADE, blank=True, null=True)
    # fotoPerfil = models.ImageField()