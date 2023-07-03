from django.db import models

# Create your models here.
class Student(models.Model):
    s_id=models.CharField(max_length=220)
    name=models.CharField(max_length=220)
    age=models.IntegerField()
    address=models.CharField(max_length=220)
    mark=models.FloatField()