from django.urls import path

from route.views import cart_add, cart_detail, cart_remove, route_save, route_archive, route_archive_detail

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<product_id>', cart_add, name='cart_add'),
    path('remove/<product_id>', cart_remove, name='cart_remove'),
    path('checkout/', route_save, name='route_save'),
    path('archive/', route_archive, name='route_archive'),
    path('archive/<int:pk>/', route_archive_detail, name='date_archive')
]
