from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from client.models import ClientObjectsProfile
from client.serializers import ClientListSerializer
from route.serializers import RouteCreateSerializer
from .cart import Cart
from dotenv import load_dotenv
import os


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ClientObjectsProfile, id=product_id)
    cart.add(product=product)
    return redirect('/client/client_list')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ClientObjectsProfile, id=product_id)
    cart.remove(product)
    return redirect('/route/')


def cart_detail(request):

    cart = Cart(request)
    ids = cart.get_ids()
    data = ClientListSerializer.get_objects(request, pk=None, ids=ids)
    total_quantity = len(data['client_obj'])

    load_dotenv()
    g_key = os.getenv("GOOGLE_API_KEY")
    maps_url = f'https://maps.googleapis.com/maps/api/js?key={g_key}&callback=initMap'

    return render(request, 'detail.html', {
        'cart': cart,
        'clients': data['client_names'],
        'addresses': data['client_obj'],
        'quantity': total_quantity,
        'url': maps_url
    })


def route_save(request):

    cart = Cart(request)
    ids = cart.get_ids()
    ids = [str(i) for i in ids]
    user = request.user.email
    data = {
        'email': user,
        'client_ids': ','.join(ids)
    }

    serializer = RouteCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.create(data)

    cart.clear()

    return redirect('client_objects_list')
