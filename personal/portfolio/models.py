from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=200)
    work = models.CharField(max_length=300)
    dob = models.CharField(max_length=100)
    email = models.TextField()
    relationship = models.CharField(max_length=200)
    callme = models.TextField()
    address = models.TextField()

class profileimg(models.Model):
    image = models.ImageField(upload_to='pics')

class about(models.Model):
    aboutme = models.TextField()


class quto(models.Model):
    quto = models.TextField()


class career(models.Model):
    header = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    joined = models.TextField()
    about = models.TextField()


class metarial(models.Model):
    coderdegree = models.TextField(max_length=100)
    cmplet_project = models.TextField(max_length=200)
    satisfied_client = models.TextField(max_length=200)
    finished = models.TextField(max_length=200)

