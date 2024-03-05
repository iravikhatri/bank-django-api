from django.db import models


class Bank(models.Model):

    name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Bank(name:{self.name}, branch: {self.branch})"
