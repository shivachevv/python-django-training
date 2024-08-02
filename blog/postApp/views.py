from django.http import HttpRequest
from django.shortcuts import render, redirect
from .services import blogpost, reactions
from . import forms
from django.contrib.auth.decorators import login_required
from .models import BlogPost


def blog_posts_home_controller(request: HttpRequest):
    payload = blogpost.get_posts(request.user.id)
    return render(request, 'blog_posts.html', {'blogs': payload})


def blog_post_controller(request: HttpRequest, id):
    payload = blogpost.get_post(id)

    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog_post = BlogPost.objects.get(id=id)
            comment.save()
            return redirect('postApp:blog', id=id)
    else:
        form = forms.CreateComment()
    return render(request, 'blog_post.html', {'blog': payload, 'comment_form': form})


@login_required(login_url="auth/login")
def create_blog_post_controller(request: HttpRequest):
    if request.method == 'POST':
        form = forms.CreateBlogPost(request.POST)
        if form.is_valid():
            newpost = form.save(request.user, commit=False)
            newpost.save()
            return redirect('postApp:blog_posts')
    else:
        form = forms.CreateBlogPost()
    return render(request, 'new_blog_post.html', {'form': form})


@login_required(login_url="auth/login")
def create_reaction_up_controller(request: HttpRequest, id):

    reactions.create_reaction('up', request, id)
    return redirect('postApp:blog_posts')


@login_required(login_url="auth/login")
def create_reaction_down_controller(request: HttpRequest, id):

    reactions.create_reaction('down', request, id)
    return redirect('postApp:blog_posts')
