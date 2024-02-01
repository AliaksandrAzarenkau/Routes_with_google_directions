from django.urls import path

from .views import cart_add, cart_detail, cart_remove, route_save

urlpatterns = [
    # path('client_create', views.ClientAPIVew.as_view(), name='client_create'),
    path('', cart_detail, name='cart_detail'),
    path('add/<product_id>', cart_add, name='cart_add'),
    path('remove/<product_id>', cart_remove, name='cart_remove'),
    path('checkout/', route_save, name='route_save')
]
