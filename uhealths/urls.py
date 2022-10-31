from django.urls import path
from . import views

app_name = 'uhealths'

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]