from django.contrib import admin
from forum.models import ForumPost, CommentForum

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(CommentForum)