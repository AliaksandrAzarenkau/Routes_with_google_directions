from django.urls import path

from .views import ClientAPIVew, ClientProfileAPIVew

urlpatterns = [
    path('client_create', ClientAPIVew.as_view(), name='create_client'),
    path('client_profile', ClientProfileAPIVew.as_view(), name='client_profile')
]
