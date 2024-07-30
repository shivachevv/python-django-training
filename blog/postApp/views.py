from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import services


def blog_posts_home_controller(request: HttpRequest):
    payload = services.get_posts(request.user.id)
    return render(request, 'blog_posts.html', {'blogs': payload})


def blog_controller(request: HttpRequest, id):
    payload = services.get_post(id)
    return render(request, 'blog_post.html', {'blog': payload})
