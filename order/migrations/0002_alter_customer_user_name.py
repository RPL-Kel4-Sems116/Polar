# Generated by Django 4.0 on 2022-05-22 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', unique=True),
        ),
    ]
