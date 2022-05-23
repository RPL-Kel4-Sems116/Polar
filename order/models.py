from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user_name = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    CHOICES = (('Graphic Design', 'Graphic Design'),('Photography', 'Photography'),('Art Project', 'Art Project'))
    services = models.CharField(choices=CHOICES,max_length=200)

    def __str__(self):
        return "{}.{}".format(self.id,self.full_name)
    