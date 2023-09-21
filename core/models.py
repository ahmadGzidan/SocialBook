from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime 
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_images',default='social-media-chatting-online-blank-profile-picture.jpg')
    location=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    relationship=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=255)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    image =models.ImageField(upload_to='post_images',null=True)
    caption =models.TextField(null=True)
    created_at =models.DateTimeField(default=datetime.now)
    no_of_likes =models.IntegerField(default=0)

    def __str__(self):
        return self.user

class likePost(models.Model):

    post_id=models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class followersCount(models.Model):
    follower = models.CharField(max_length=255)
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.user

