import os

from django.contrib.auth.models import AbstractUser
from django.db import models

class crudstudent(models.Model):
    time=models.DateTimeField(auto_now_add=True)

    name_ko=models.CharField(max_length=100)
    name_en=models.CharField(max_length=100)
    service= models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    device=models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to='')
    crc=models.CharField(max_length=100)
    imageFile = models.FileField(upload_to='')

class zebal(models.Model):
    id2=models.CharField(max_length=10)

    time2=models.DateTimeField(auto_now_add=True)

    name_ko2=models.CharField(max_length=100)
    name_en2=models.CharField(max_length=100)
    service2= models.CharField(max_length=100)
    product2=models.CharField(max_length=100)
    device2=models.CharField(max_length=100)
    uploadedFile2 = models.FileField(upload_to='')
    crc2=models.CharField(max_length=100)
    imageFile2 = models.FileField(upload_to='')

class miribogi(models.Model):
    id3=models.CharField(max_length=10)

    time3=models.DateTimeField(auto_now_add=True)

    name_ko3=models.CharField(max_length=100)
    name_en3=models.CharField(max_length=100)
    service3= models.CharField(max_length=100)
    product3=models.CharField(max_length=100)
    device3=models.CharField(max_length=100)
    uploadedFile3 = models.FileField(upload_to='')
    crc3=models.CharField(max_length=100)
    imageFile3 = models.FileField(upload_to='')