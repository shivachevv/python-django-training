from django.http import HttpRequest
from .models import BlogPost, BlogPostReaction, Comment, Reaction
from .utils import BlogPostUtils


def get_posts(user_id: int):
    blogposts = BlogPost.objects.all().filter(user_id=user_id)

    result = []

    for blogpost in blogposts:
        reactions = blogpost.reactions.all().values()
        comments = blogpost.comments.all().values()

        result.append({
            'id': blogpost.id,
            'title': blogpost.title,
            'author': f'{blogpost.user.first_name} {blogpost.user.last_name}',
            'reactions': BlogPostUtils.prettify_reactions(reactions),
            'comments': len(comments),
        })

    return result
