from django.http import HttpRequest
from .models import BlogPost, BlogPostReaction, Comment, Reaction


def get_posts(user_id: int):

    blogs = BlogPost.objects.all().filter(
        user_id=user_id).select_related('reactions')
    print('blogs', blogs.values())
    # print('service', request.user.id)
    return [
        {
            "title": "TITLE 1"
        }
    ]
