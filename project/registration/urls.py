from django.urls import path

from .views import RegistrationAPIVew, LoginAPIView, LogoutAPIView, GetCurrentUserAPIVew


urlpatterns = [
    path('user_create', RegistrationAPIVew.as_view(), name='registration'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('current_user', GetCurrentUserAPIVew.as_view(), name='current_user'),
]
