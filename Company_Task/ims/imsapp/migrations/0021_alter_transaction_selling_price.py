# Generated by Django 4.2.5 on 2023-10-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0020_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
