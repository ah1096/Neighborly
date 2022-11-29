from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    biotext = models.TextField(max_length=300, default=None, null=True)
    skills = models.ManyToManyField('Skill', related_name="user_list")

    def __str__(self):
        return self.username


class Skill(models.Model):
    skill = models.TextField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.skill
