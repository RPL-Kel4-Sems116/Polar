# Generated by Django 4.0 on 2022-05-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_customer_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='services',
            field=models.CharField(choices=[('Graphic Design', 'Graphic Design'), ('Photography', 'Photography'), ('Art Project', 'Art Project')], default='Graphic Design', max_length=200),
        ),
    ]