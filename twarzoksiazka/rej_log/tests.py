from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from rej_log.models import User, User_details
from posts.models import Post, Comment, Like

# Create your tests here.


class Rej_logPageTests(SimpleTestCase):
    
    
    def test_hello(self):
        response = reverse('hello')
        assert resolve(response).view_name == 'hello'
        
    def test_register(self):
        response = reverse('register')
        assert resolve(response).view_name == 'register'
    
    def test_login(self):
        response = reverse('login')
        assert resolve(response).view_name == 'login'
        
    def test_update(self):
        response = reverse('update')
        assert resolve(response).view_name == 'update'
        
    def test_search(self):
        response = reverse('profile-search')
        assert resolve(response).view_name == 'profile-search'
        
    def test_add_friend(self):
        response = reverse('add-friend')
        assert resolve(response).view_name == 'add-friend'
        
    def test_show_invitations(self):
        response = reverse('show_infitations')
        assert resolve(response).view_name == 'show_infitations'
        
    def test_accept_invite(self):
        response = reverse('accept_invite')
        assert resolve(response).view_name == 'accept_invite'
        
        
    