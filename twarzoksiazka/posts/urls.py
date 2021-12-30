from django.urls import path
from .views import post_com_upload, like_unlike

app_name = 'posts'

urlpatterns = [
    path('', post_com_upload, name='post-com-upload'),
    path('liked/', like_unlike, name='like-post-view'),
]
