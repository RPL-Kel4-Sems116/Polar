# Generated by Django 4.0 on 2022-05-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_customer_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.CharField(default='  ', max_length=200),
        ),
    ]
