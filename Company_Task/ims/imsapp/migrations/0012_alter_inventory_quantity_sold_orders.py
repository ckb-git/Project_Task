# Generated by Django 4.2.5 on 2023-10-03 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0011_alter_inventory_iin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity_sold',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('t_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.inventory')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
