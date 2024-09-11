# Generated by Django 5.1.1 on 2024-09-09 09:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_remove_food_deleted_at_remove_food_restored_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['name'], name='foods_name_01bd69_idx'),
        ),
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['price'], name='foods_price_7dd83c_idx'),
        ),
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['name', 'price'], name='foods_name_b96160_idx'),
        ),
    ]
