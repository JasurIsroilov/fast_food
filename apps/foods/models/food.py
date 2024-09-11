from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class Food(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    user = models.ForeignKey("account.User", on_delete=models.PROTECT, related_name="foods")
    category = models.ForeignKey("foods.FoodsCategory", on_delete=models.PROTECT, related_name="foods")

    class Meta:
        db_table = "foods"
        indexes = [
            models.Index(fields=[
                'name',
            ]),
            models.Index(fields=[
                'price',
            ]),
            models.Index(fields=[
                'name',
                'price'
            ]),
        ]

    def __str__(self):
        return self.name
