# Generated by Django 4.0 on 2022-05-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_customer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(default='  ', max_length=200),
        ),
    ]
