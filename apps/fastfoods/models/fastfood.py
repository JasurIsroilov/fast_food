from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class FastFood(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=150, null=False, name=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=False, blank=False)

    food = models.ManyToManyField("foods.Food", blank=False)

    class Meta:
        db_table = "fast_foods"
        indexes = [
            models.Index(fields=[
                'name',
            ]),
        ]

    def __str__(self):
        return self.name
