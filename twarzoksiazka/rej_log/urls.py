from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register),
    path('hello/',views.hello_login),

    path('login/',views.viev_login),
]
