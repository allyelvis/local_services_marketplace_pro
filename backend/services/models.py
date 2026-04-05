
from django.db import models
from users.models import User

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
