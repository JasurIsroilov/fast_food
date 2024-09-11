from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class OrderItem(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    quantity = models.PositiveIntegerField(null=False, blank=False)
    food = models.ForeignKey("foods.Food", related_name="order_items", on_delete=models.PROTECT)
    order = models.ForeignKey("orders.Order", related_name="order_items", on_delete=models.PROTECT)

    class Meta:
        db_table = "order_items"
        indexes = [
            models.Index(fields=[
                'order',
            ]),
        ]

    def __str__(self):
        return f"OrderItem #{self.id}"
