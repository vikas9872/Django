from django.db import models

# Create your models here.
class appointment(models.Model):
    fname=models.CharField(max_length=16)
    lname=models.CharField(max_length=16)
    age=models.IntegerField()
    date=models.DateField(null=True)


