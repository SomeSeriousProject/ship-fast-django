from uuid import uuid4
from django.db import models
from django.utils.timezone import datetime


class SoftDeleteManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return (
            super()
            .get_queryset()
            .filter(
                deleted_at=None,
                is_active=True,
            )
        )


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now()
        return self.save()

    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
