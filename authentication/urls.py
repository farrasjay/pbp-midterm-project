from django.urls import path
from .views import index, login_user, register_user, logout_user, login_flutter

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login-flutter/', login_flutter, name='login_flutter'),
]