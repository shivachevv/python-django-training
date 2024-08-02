from django import forms
from .models import BlogPost, Comment, Hashtag


class CreateBlogPost(forms.ModelForm):
    hashtags = forms.CharField(
        max_length=200, required=False, help_text="Enter hashtags separated by commas")

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'hashtags']

    def save(self, user, commit=True):
        instance = super().save(commit=False)
        instance.user = user
        hashtags_str = self.cleaned_data['hashtags']
        hashtags = [Hashtag.objects.get_or_create(
            name=tag.strip())[0] for tag in hashtags_str.split(',')]
        if commit:
            instance.save()
            instance.hashtags.set(hashtags)
        return instance


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
