from django.db import models
# Create your models here.
class sign(models.Model):
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)

class details(models.Model):
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone = models.IntegerField()