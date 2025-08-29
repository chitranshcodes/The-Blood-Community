from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class BRequest(models.Model):
    user=models.ForeignKey(User, related_name='brequests' , on_delete=models.CASCADE)
    bgroup=models.CharField(max_length=4)
    time=models.DateTimeField(default=timezone.now)
    district=models.CharField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    district=models.CharField()
    bgroup=models.CharField()