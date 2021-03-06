from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_hr_department   = models.BooleanField(default=False)
    is_fin_department  = models.BooleanField(default=False)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)