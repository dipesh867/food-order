# Generated by Django 5.1.2 on 2025-03-24 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0009_orders_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cost',
        ),
    ]
