from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 



class UserTag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=100)
    story = models.TextField()
    tag = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.headline

class TopFeatured(models.Model):
    headline = models.CharField(max_length=100)
    story = models.TextField()
    tag = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=300, default="")


    