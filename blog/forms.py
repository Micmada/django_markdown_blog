from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
