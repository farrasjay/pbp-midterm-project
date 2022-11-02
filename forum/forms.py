from django import forms
from .models import *

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForum
        fields = ['description']