# Generated by Django 4.0 on 2022-05-24 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('order', '0007_alter_customer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
