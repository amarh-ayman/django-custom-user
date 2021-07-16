from django.contrib.auth.forms import UserChangeForm,UserCreationForm ,AuthenticationForm
from .models import CustomUser
from django.db import models

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model =CustomUser
    fields=('username','email','full_name')

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model =CustomUser
    fields=('username','email')


