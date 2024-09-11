from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class FoodsCategory(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = "foods_categories"
        verbose_name_plural = "Food categories"

    def __str__(self):
        return self.name
