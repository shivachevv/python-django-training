from django.urls import path
from . import views

app_name = 'postApp'

urlpatterns = [
    path('', views.blog_posts_home_controller, name='blog_posts'),
]
