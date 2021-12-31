from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from rej_log.models import User, User_details
from posts.models import Post, Comment, Like
from mixer.backend.django import mixer

# Create your tests here.


class Rej_logPageTests(TestCase):
    
    
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
        
    def test_user_det(self):
        details = mixer.blend('rej_log.User_details', bio='Jakis opis profilu', name='Jakub', surr_name='Matuszak')
        assert details.bio == 'Jakis opis profilu' and details.name == 'Jakub' and details.surr_name == 'Matuszak'
    
    def test_friend(self):
        friend = mixer.blend('rej_log.Relationship', status='friend')
        assert friend.status == 'friend'
        
    