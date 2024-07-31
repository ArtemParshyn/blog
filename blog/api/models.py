from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ...


class Comment(models.Model):
    description = models.CharField(blank=False, max_length=255)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)


class Blog(models.Model):
    description = models.CharField(blank=True, max_length=255)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="blog", on_delete=models.CASCADE)
    likes = models.IntegerField()
