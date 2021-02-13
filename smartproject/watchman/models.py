from django.db import models
from django.utils import timezone
import math

# Create your models here.

class Watchman(models.Model):
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30,blank=True)
    address=models.CharField(max_length=100,blank=True)
    contact_no=models.CharField(max_length=30,blank=True)
    family_contact_no=models.CharField(max_length=30,blank=True)
    age=models.CharField(max_length=30,blank=True)
    blood_group=models.CharField(max_length=30,blank=True)
    photo_id=models.FileField(upload_to='images/',blank=False)
    profile_picture=models.FileField(upload_to='images/',default="defaultpic.png")
    status=models.CharField(max_length=30,default="Pending")

    def __str__(self):
        return self.firstname

class Visitor(models.Model):
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    address=models.CharField(max_length=100,blank=True)
    contact_no=models.CharField(max_length=30,blank=True)
    created_at=models.DateTimeField(blank=False,default=timezone.now)
    updated_at=models.DateTimeField(blank=False,default=timezone.now)

    def __str__(self):
        return self.firstname