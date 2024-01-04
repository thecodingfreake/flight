# models.py

from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class flightdeatils(models.Model):
    name=models.CharField(max_length=2080)
    refno=models.CharField(max_length=2080,default='123')
    time=models.TimeField()
    fromp=models.CharField(max_length=2080)
    top=models.CharField(max_length=2080)
    date=models.DateField()
    seats=models.IntegerField()

class flightbookings(models.Model):
    user=models.CharField(max_length=2080)
    refno=models.CharField(max_length=2080)
    name=models.CharField(max_length=2080)
    time=models.TimeField()
    fromp=models.CharField(max_length=2080)
    top=models.CharField(max_length=2080)
    date=models.DateField()
    seats=models.IntegerField()