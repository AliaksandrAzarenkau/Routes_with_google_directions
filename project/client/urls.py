from django.urls import path

from .views import ClientAPIVew, ClientProfileAPIVew

urlpatterns = [
    path('client', ClientAPIVew.as_view(), name='client'),
    path('client_profile', ClientProfileAPIVew.as_view(), name='client_profile')
]
