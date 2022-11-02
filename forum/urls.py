from django.urls import path
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', index, name='Forum'),
    path('posts/<int:id>/', forum_post_detail, name="detail"),
    path('api/ForumList/', get_forum_list, name="getForumList"),
    path('api/addForum/', create_post_ajax, name="addNewForum"),
    path('api/comment/<int:id>/', get_comment_list, name="getCommentList"),
    path('api/addComment/<int:id>/', create_comment_ajax, name="addNewComment"),
    path('deleteForum/<int:id>/', delete_forum, name="deleteForum"),
    path('deleteComment/<int:id>/', delete_comment, name="deleteComment")
]