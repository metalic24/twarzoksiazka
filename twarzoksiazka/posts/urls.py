from django.urls import path
from .views import post_com_upload, like_unlike, Delete_Post, Update_Post

app_name = 'posts'

urlpatterns = [
    path('', post_com_upload, name='post-com-upload'),
    path('liked/', like_unlike, name='like-post-view'),
    path('<pk>/delete/', Delete_Post.as_view(), name='delete-post'),
    path('<pk>/update/', Update_Post.as_view(), name='update-post'),
]
