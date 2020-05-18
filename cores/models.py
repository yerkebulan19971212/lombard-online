import uuid as uuid_lib

# django imports
from django.db import models


class Category(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    title = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        full_name_of_category = [self.title]

        parent = self.parent

        while parent:
            full_name_of_category.append(parent.title)
            parent = parent.parent

        return " -> ".join(full_name_of_category)
