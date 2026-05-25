# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Slot(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='available')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)