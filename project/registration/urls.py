from django.urls import path

from .views import RegistrationAPIVew, LoginAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    path('registration', RegistrationAPIVew.as_view(), name='registration'),
    path('registration/login', LoginAPIView.as_view(), name='login'),
    path('user', UserRetrieveUpdateAPIView.as_view(), name='profile update'),
]
