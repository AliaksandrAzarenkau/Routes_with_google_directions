from django.urls import path

from .views import post, get

urlpatterns = [
    path('add/', post),
    path('get/', get)
]
