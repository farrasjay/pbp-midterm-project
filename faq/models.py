from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    # liked = models.IntegerField()
    liked =  models.ManyToManyField(User, blank=True, related_name='likes')
    num_liked = models.IntegerField(default=0)
    def num_likes(self):
        return self.liked.all().count()

    def has_been_liked(self):
        return self.liked is not None

class Like(models.Model): 
    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    question_like = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuestionForm(models.Model):
    user_form = models.ForeignKey(User, on_delete=models.CASCADE)
    question_in_form = models.TextField()

