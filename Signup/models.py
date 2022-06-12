from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=1000)
    age=models.IntegerField()

class Bio(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    gender=models.CharField(max_length=50)
    pic=models.EmailField(max_length=50)
    dOb=models.DateField()
    country=models.CharField(max_length=100)