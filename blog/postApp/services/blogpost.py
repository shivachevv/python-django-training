from django.shortcuts import get_object_or_404
from ..models import BlogPost
from ..utils import BlogPostUtils


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


def get_post(id):
    blogpost = get_object_or_404(BlogPost, pk=id)
    reactions = blogpost.reactions.all().values()
    comments = blogpost.comments.all().select_related('user')

    return {
        'id': blogpost.id,
        'title': blogpost.title,
        'content': blogpost.content,
        'author': f'{blogpost.user.first_name} {blogpost.user.last_name}',
        'reactions': BlogPostUtils.prettify_reactions(reactions),
        'comments': comments,
        'comments_count': len(comments),
    }
