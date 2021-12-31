from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from rej_log.models import User, User_details
from posts.models import Post, Comment, Like
from mixer.backend.django import mixer

# Create your tests here.


class PostTests(TestCase):
    
    def test_content(self):
        post = mixer.blend('posts.Post', content='Jakis post')
        assert post.content == 'Jakis post'
        
    def test_comment(self):
        comment = mixer.blend('posts.Comment', com_body='Jakis komentarz')
        assert comment.com_body == 'Jakis komentarz'