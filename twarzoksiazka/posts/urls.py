from django.urls import path
from .views import post_com_upload

urlpatterns = [
    path('', post_com_upload),
]
