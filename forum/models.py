from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    topic = models.CharField(max_length=140)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)

class CommentForum(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parentForum = models.ForeignKey(ForumPost, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
