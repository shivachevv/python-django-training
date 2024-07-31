from django import forms
from .models import BlogPost, Comment


class CreateBlogPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
