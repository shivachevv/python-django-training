from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from . import services
from . import forms
from django.contrib.auth.decorators import login_required


def blog_posts_home_controller(request: HttpRequest):
    payload = services.get_posts(request.user.id)
    return render(request, 'blog_posts.html', {'blogs': payload})


def blog_post_controller(request: HttpRequest, id):
    payload = services.get_post(id)
    return render(request, 'blog_post.html', {'blog': payload})


@login_required(login_url="auth/login")
def create_blog_post_controller(request: HttpRequest):
    if request.method == 'POST':
        form = forms.CreateBlogPost(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.save()
            return redirect('postApp:blog_posts')
    else:
        form = forms.CreateBlogPost()
    return render(request, 'new_blog_post.html', {'form': form})
