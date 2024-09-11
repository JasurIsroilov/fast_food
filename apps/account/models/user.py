from django.db import models
from django.contrib.auth.models import AbstractUser
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin


class User(AbstractUser, SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE

    phone_number = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def activate(self, method):
        if method == "POST":
            self.is_active = True
        elif method == "DELETE":
            self.is_active = False
        else:
            pass
        self.save()

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=[
                'username',
            ]),
            models.Index(fields=[
                'phone_number',
            ]),
            models.Index(fields=[
                'first_name',
            ]),
            models.Index(fields=[
                'last_name',
            ]),
            models.Index(fields=[
                'email',
            ]),
        ]

    def __str__(self):
        return self.username
