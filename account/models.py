from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']