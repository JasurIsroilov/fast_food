# Generated by Django 5.1.1 on 2024-09-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_food_deleted_at_food_restored_at_food_transaction_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='food',
            name='restored_at',
        ),
        migrations.RemoveField(
            model_name='food',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='foodscategory',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='foodscategory',
            name='restored_at',
        ),
        migrations.RemoveField(
            model_name='foodscategory',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='food',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='foodscategory',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='foodscategory',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
