from django.urls import path
from . import views

app_name = 'postApp'

urlpatterns = [
    path('', views.blog_posts_home_controller, name='blog_posts'),
    path('new-post', views.create_blog_post_controller, name='create_blog_post'),
    path('<int:id>', views.blog_post_controller, name="blog"),
]
