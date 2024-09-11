from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class Order(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    STATUS_CHOICES = (
        ('ordered', _('Ordered')),
        ('accepted', _('Accepted')),
        ('sent', _('Sent')),
        ('completed', _('Completed'))
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="ordered", blank=False, null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    delivery_at = models.DateTimeField(blank=True, null=False)

    user = models.ForeignKey("account.User", related_name="orders", on_delete=models.PROTECT)
    fastfood = models.ForeignKey("fastfoods.FastFood", related_name="orders", on_delete=models.PROTECT)

    class Meta:
        db_table = "orders"
        indexes = [
            models.Index(fields=[
                'status',
            ]),
            models.Index(fields=[
                'created_at',
            ]),
            models.Index(fields=[
                'user',
            ]),
            models.Index(fields=[
                'status',
                'created_at',
            ]),
        ]

    def __str__(self):
        return f"Order #{self.id}"
