from django.db import models

# Create your models here.
class Post(models.Model):
    full_name = models.CharField(max_length=300, unique=True)
    email = models.CharField(max_length=40, unique=True)
    number = models.CharField(max_length=40, unique=True)
    password1 = models.CharField(max_length=40, unique=True)
    password2 = models.CharField(max_length=40, unique=True)