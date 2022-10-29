from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('', views.show_faq_page, name='faq'),
    path('/like/', views.like_unlike_post, name='like'),

]