from django.http import HttpRequest
from ..models import BlogPost, BlogPostReaction, Reaction
from typing import Literal


def create_reaction(type: Literal['up', 'down'], request: HttpRequest, id):
    reaction_name = "thumb_up" if type == 'up' else "thumb_down"

    blogpost = BlogPost.objects.get(id=id)
    reaction = Reaction.objects.get(name=reaction_name)

    BlogPostReaction.objects.create(
        blog_post=blogpost, reaction=reaction, user=request.user)
