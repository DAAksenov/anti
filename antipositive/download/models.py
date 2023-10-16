from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

class PKL(models.Model):
    pkl = models.CharField(max_length=100)
