from django.db import models

# Create your models here.
from django.db import models
import uuid

class AuditModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True