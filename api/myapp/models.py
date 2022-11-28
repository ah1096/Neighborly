from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser) :
    biotext = models.TextField(max_length=300, default=None, null=True)

    def __str__(self):
        return self.username

