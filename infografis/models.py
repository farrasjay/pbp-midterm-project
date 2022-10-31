from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.TextField(blank=True, null=True)
    date = models.DateField()
    comment = models.TextField()

class Commentkedua(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.TextField(blank=True, null=True)
    date = models.DateField()
    comment = models.TextField()

class Commentketiga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.TextField(blank=True, null=True)
    date = models.DateField()
    comment = models.TextField()