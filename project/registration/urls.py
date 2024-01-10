from django.urls import path

from .views import CreateUserView, UpdateUserView


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/', UpdateUserView.as_view(), name='update'),
]
