from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    postTitle = models.CharField(max_length=255)
    postDesc = models.TextField(null=True)
    postContent = models.TextField()
    user = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)