# Generated by Django 4.0 on 2022-05-24 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_customer_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='full_name',
        ),
    ]
