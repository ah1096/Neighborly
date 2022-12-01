from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    biotext = models.TextField(max_length=300, default=None, null=True)
    skills = models.ManyToManyField('Skill', related_name="user_list")

    role = models.ForeignKey('Role', on_delete=models.DO_NOTHING, default=None, null=True)
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING, default=None, null=True, related_name="user_list")

    def __str__(self):
        return self.username


class Skill(models.Model):
    skill = models.TextField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.skill



#https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices
class Role(models.Model):
    USER = "US"
    MAKER = "MA"
    FIXER = "FI"
    TEACHER = "TE"
    HELPER = "HE"

    ROLE_CHOICES = [
        (USER, 'User'),
        (MAKER, 'Maker'),
        (FIXER, 'Fixer'),
        (TEACHER, 'Teacher'),
        (HELPER, 'Helper'),
    ]

    role_tag = models.CharField(
        max_length = 2,
        choices = ROLE_CHOICES,
        default=USER,
    )

    def __str__(self):
        return self.role_tag

class Location(models.Model):
    location = models.TextField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.location


