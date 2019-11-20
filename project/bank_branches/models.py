from django.db import models

class Banks(models.Model):

    ifsc = models.CharField(max_length=15)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=50)
