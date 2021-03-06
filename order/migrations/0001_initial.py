# Generated by Django 4.0 on 2022-05-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=12)),
                ('services', models.CharField(choices=[('Graphic Design', 'Graphic Design'), ('Photography', 'Photography'), ('Art Project', 'Art Project')], max_length=200)),
            ],
        ),
    ]
