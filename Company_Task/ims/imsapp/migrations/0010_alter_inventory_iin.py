# Generated by Django 4.2.5 on 2023-10-01 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0009_alter_inventory_iin_alter_inventory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
