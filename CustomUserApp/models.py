from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser ,models.Model):
  full_name =models.CharField(max_length=64)
  def __str__(self):
    return self.username

