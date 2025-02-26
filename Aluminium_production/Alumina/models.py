from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)
    Mail=models.CharField(max_length=100)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Status=models.BooleanField(default=False)
    