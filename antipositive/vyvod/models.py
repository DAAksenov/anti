from django.db import models
from django.contrib.postgres.fields import ArrayField


class Test(models.Model):
    name = models.CharField(max_length=100)


class Data(models.Model):
    array1 = models.TextField()
    array2 = models.TextField()
    
