from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class BRequest(models.Model):
    user=models.ForeignKey(User, related_name='brequests' , on_delete=models.CASCADE)
    bgroup=models.CharField(max_length=4)
    time=models.DateTimeField(default=timezone.now)
    district=models.CharField(max_length=100)

    def  __str__(self):
        return f"{self.bgroup} in {self.district} by {self.user}"


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    district=models.CharField(max_length=100)
    bgroup=models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+919876543210'. Up to 15 digits allowed."
    )
    phone=models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)

    def  __str__(self):
        return f"{self.bgroup}, {self.district}, {self.user}"
    
class Post(models.Model):
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content=models.TextField(default='Express something')
    time=models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)

    def __str__(self):
        return self.title