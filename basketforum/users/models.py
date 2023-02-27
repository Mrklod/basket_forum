from django.db import models
from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
    biografy = models.TextField(blank=True)

