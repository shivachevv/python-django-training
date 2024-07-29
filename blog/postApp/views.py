from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import services


def blog_posts_home_controller(request: HttpRequest):
    payload = services.get_posts(request.user.id)
    print('Controller payload', payload)
    return render(request, 'blog_posts.html', {'blogs': payload})
