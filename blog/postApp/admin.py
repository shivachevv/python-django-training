from django.contrib import admin

from .models import BlogPost, BlogPostReaction, Comment, Reaction

# Register your models here.

admin.site.register(Reaction)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(BlogPostReaction)
