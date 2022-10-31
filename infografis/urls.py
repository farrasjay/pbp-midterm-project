from django.urls import path
from . import views

app_name = 'infografis'

urlpatterns = [
    path('', views.infografis, name='infografis'),
    path('infografis/', views.infografis, name='infografis'),
    path('artikel1/', views.first_artikel, name='first_artikel'),
    path('artikel2/', views.second_artikel, name='second_artikel'),
    path('artikel3/', views.third_artikel, name='third_artikel'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('add_comment2/', views.add_commentkedua, name='add_commentkedua'),
    path('add_comment3/', views.add_commentketiga, name='add_commentketiga'),
    path('json/', views.show_json1, name='show_json1'),
    path('jsonkedua/', views.show_json2, name='show_json2'),
    path('jsonketiga/', views.show_json3, name='show_json3'),
]