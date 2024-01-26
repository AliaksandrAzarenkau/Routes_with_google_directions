from django.urls import path

from registration import views


urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('user_create', views.RegistrationAPIVew.as_view(), name='registration'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('logout', views.LogoutAPIView.as_view(), name='logout'),
    path('current_user', views.GetCurrentUserAPIVew.as_view(), name='current_user'),
    path('user_profile', views.UserEditProfileAPIView.as_view(), name='user_profile'),
    path('user_profile_photo', views.UserPhotoView.as_view(), name='user_profile_photo'),
]
