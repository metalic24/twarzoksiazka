from django import forms
from django.forms import fields
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Co masz na twarzy?', 'rows': 3, 'cols': 60}))
    class Meta:
        model = Post
        fields = (
            'content',
            'post_img',
        )
        
class CommentForm(forms.ModelForm):
    com_body = forms.CharField(label='Comment ', widget=forms.TextInput(attrs={'placeholder': 'Add comment'}))
    class Meta:
        model = Comment
        fields = (
            'com_body',
        )