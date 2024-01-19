from django.db import models
from django.db.models.query import QuerySet
import uuid


# Create Custom Model manager that return only not deleted data(i.e, soft-deleted)
class CustomManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)



# Create Base Model for all other Models that is created in Project that contain soft-delete functionality
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = CustomManager()  # overwrite with custom model manager
    every = models.Manager()  # create new model manage that works as built in model manager

    def delete_obj(self):
        self.is_deleted = True
        self.save()

    def restore_obj(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True  # It indicates that this class is not model, but it is a base class for models
