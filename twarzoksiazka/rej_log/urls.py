from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.register, name='register'),
    path('hello/',views.hello_login, name='hello'),

    path('login/',views.viev_login, name='login'),
    path('logout/',views.log_out, name='log-out'),
    path('update/',views.update_user_details, name='update'),
    path('search/',views.get_profiles, name='profile-search'),
    path('add_friend/',views.add_friend, name='add-friend'),
    path('show_infitations/',views.show_infitations, name='show_infitations'),
    path('accept_invite/',views.accept_invite, name='accept_invite'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),

]
