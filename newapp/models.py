from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
class Login(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    type = models.IntegerField()
class Service(models.Model):
    img = models.FileField()
    head = models.CharField(max_length=100)
    data = models.CharField(max_length=1000)
class Project(models.Model):
    img = models.FileField()
    head = models.CharField(max_length=100)
    data = models.CharField(max_length=1000)
