from django.urls import path

from client import views

urlpatterns = [
    path('client_create', views.ClientAPIVew.as_view(), name='client_create'),
    path('client_profile', views.ClientProfileAPIVew.as_view(), name='client_profile'),
    path('client_list', views.ClientListAPIView.as_view(), name='client_list'),
    path('client_objects_list', views.ClientListAPIView.as_view(), name='client_objects_list'),
    path('client_objects_list/<int:pk>', views.ClientObjectsListAPIView.as_view(), name='objects'),
]
