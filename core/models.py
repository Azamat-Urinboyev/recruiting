from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    state = models.CharField(max_length=50)
    rate = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    experience = models.CharField(max_length=25)


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    rate_cpm = models.CharField(max_length=20)
    rate_per = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    experience = models.CharField(max_length=25)