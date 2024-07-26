from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Reaction(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reactions = models.ManyToManyField(
        Reaction,
        through="BlogPostReaction",
        through_fields=("blog_post", "reaction"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)


def __str__(self):
    return self.title


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.content


class BlogPostReaction(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reaction_user",
    )
