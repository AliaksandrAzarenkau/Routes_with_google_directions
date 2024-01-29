from django.urls import path

from .views import ClientAPIVew, ClientProfileAPIVew, ClientListAPIView, ClientObjectsListAPIView

urlpatterns = [
    path('client_create', ClientAPIVew.as_view(), name='client_create'),
    path('client_profile', ClientProfileAPIVew.as_view(), name='client_profile'),
    path('client_list', ClientListAPIView.as_view(), name='client_list'),
    path('client_objects_list', ClientListAPIView.as_view(), name='client_objects_list'),
    path('client_objects_list/<int:pk>', ClientObjectsListAPIView.as_view(), name='objects')
]
