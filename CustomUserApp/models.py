from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUser(AbstractUser):
  full_name =models.CharField(max_length=64)
  USERNAME_FIELD='email'
  email = models.EmailField(_('email address'), unique=True)
  REQUIRED_FIELDS=[]

  def __str__(self):
    return self.username
  
  

