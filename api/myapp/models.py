from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    biotext = models.TextField(max_length=300, default=None, null=True)
    skills = models.ManyToManyField('Skill', related_name="user_list")
    role = models.ForeignKey('Role', on_delete=models.DO_NOTHING, default=None, null=True, related_name="user_list")
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING, default=None, null=True, related_name="user_list")

    def __str__(self):
        return self.username


class Skill(models.Model):
    skill = models.TextField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.skill


#https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices
class Role(models.Model):

    role_tag = models.CharField(
        max_length = 10,
        default="User",
    )

    def __str__(self):
        return self.role_tag


class Location(models.Model):
    location = models.TextField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.location



# EXCHANGE TAGS, POSTS AND COMMENTS/////////////////////////////////

class Exchange(models.Model):
    exchange_tag = models.CharField(max_length=40, default=None, null=True)

    def __str__(self):
        return self.exchange_tag


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True) #creates unique URL based on the title of the post
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='user_post')
    content = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    # exTags = models.ManyToManyField(Exchange, blank=True)
    # lTags = models.ManyToManyField(Location, default=CustomUser.location)

    #image = models.ImageField(upload_to='', blank=True, null=True) --> ADD THIS LATER W/ FIREBASE

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # def save(self):
    #     if not self.ltags:
    #         user = CustomUser.objects.get(pk=self.author)
    #         self.ltags.add(user.location)
    #     super(Post, self).save(*args, **kwargs)



# do comments AFTER posts are working

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=800)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

