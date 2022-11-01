from django.urls import path
from . import views

app_name = 'uhealths'

urlpatterns = [
    path('', views.landingpage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.main_menu, name='menu'),
    path('profile/', views.show_healthstats, name='show_healthstats'),
    path('update-healthstats/', views.insert_healthstats, name='insert_healthstats'),
    path('json/', views.show_json, name="asjson"),
    path('ajax/', views.show_healthstats_ajax, name="getajax"),
    path('ajax-post/', views.post_healthstats_ajax, name="postajax")
]