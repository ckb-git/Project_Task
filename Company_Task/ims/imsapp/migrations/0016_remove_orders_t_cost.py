# Generated by Django 4.2.5 on 2023-10-04 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0015_alter_orders_item_alter_orders_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='t_cost',
        ),
    ]
