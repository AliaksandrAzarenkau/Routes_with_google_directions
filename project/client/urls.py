from django.urls import path

from .views import post, get_all

urlpatterns = [
    path('add/', post, name='add_client'),
    path('get_all/', get_all, name='get_all_clients')
]
