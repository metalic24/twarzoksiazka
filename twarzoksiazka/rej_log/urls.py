from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register),
    path('hello/',views.hello_login),

    path('login/',views.viev_login),
    path('update/',views.update_user_details),
    path('search/',views.get_profiles, name='profile-search'),
    path('add_friend/',views.add_friend, name='add-friend'),
    path('show_infitations/',views.show_infitations, name='show_infitations'),
    path('accept_invite/',views.accept_invite, name='accept_invite'),
]
