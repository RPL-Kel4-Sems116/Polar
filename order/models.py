from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user_name = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    CHOICES = (('Graphic Design', 'Graphic Design'),('Photography', 'Photography'),('Art Project', 'Art Project'))
    CHOICES2 = (('Akan dihubungi admin', 'Akan dihubungi admin'),('Proses', 'Proses'),('Selesai', 'Selesai'))
    services = models.CharField(choices=CHOICES,max_length=200, default=CHOICES[0][0])
    status = models.CharField(choices=CHOICES2,max_length=200, default=CHOICES2[0][0])

    def __str__(self):
        return "{}.{}".format(self.id,self.user_name)


class Gambar(models.Model):
    gambar = models.ImageField(upload_to='gambar')

class Gambar2(models.Model):
    gambar2 = models.ImageField(upload_to='gambar')

class Gambar3(models.Model):
    gambar3 = models.ImageField(upload_to='gambar')