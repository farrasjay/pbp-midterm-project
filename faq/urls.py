from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('/', views.show_faq_page, name='faq'),
    path('/like/<int:id>', views.like_unlike_post, name='like'),
    path('/set/<int:id>', views.set_session, name='set'),
    path('/get/', views.get_session, name='get'),
    path('/send_question/', views.send_question, name='send'),
]