from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Snack(models.Model):
  title=models.CharField(max_length=100)
  purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE ,default=1)
  description=models.TextField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('snack_list')  


