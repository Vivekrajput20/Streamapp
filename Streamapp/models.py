from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    status = models.BooleanField(default=False)