from django import forms
from django.forms import fields
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
            'post_img',
        )