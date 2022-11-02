
from email.policy import default
from random import choices
import re
from django.db import models
from django.contrib.auth.models import User

class UserHealthStatus(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    last_update = models.DateTimeField()
    
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6)

    bmr = models.FloatField()
    bmi = models.FloatField()
    calories_intake = models.IntegerField(default=0)
