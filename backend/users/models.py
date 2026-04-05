
from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
