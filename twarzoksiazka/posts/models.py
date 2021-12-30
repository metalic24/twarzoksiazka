from django.contrib.auth.models import User
from django.db import models
from rej_log.models import User_details

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    post_img = models.ImageField(upload_to='posts', blank=True)
    liked = models.ManyToManyField(User_details, default=None, related_name='likes', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User_details, on_delete=models.CASCADE, related_name='posts')
    
    def num_likes(self):
        return self.liked.all().count()
    
    def num_comments(self):
        return self.commment_set.all().count()
    
    
    class Meta:
        ordering = ('-created',)
        
class Comment(models.Model):
    user = models.ForeignKey(User_details, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com_body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
Like_Choice = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
    
class Like(models.Model):
    user = models.ForeignKey(User_details, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value =  models.CharField(choices=Like_Choice, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)