from django.urls import path
from . import views

app_name = 'postApp'

urlpatterns = [
    path('', views.blog_posts_home_controller, name='blog_posts'),
    path('new-post', views.create_blog_post_controller, name='create_blog_post'),
    path('create-reaction-up/<int:id>',
         views.create_reaction_up_controller, name="create_reaction_up"),
    path('create-reaction-down/<int:id>',
         views.create_reaction_down_controller, name="create_reaction_down"),
    path('<int:id>', views.blog_post_controller, name="blog"),
]
