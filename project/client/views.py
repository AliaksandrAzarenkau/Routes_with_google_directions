from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Client


def post(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.post(request.POST)

            """Поправить редирект"""

            return redirect('/')
        else:
            return render(request, "add_client.html", {"form": ClientForm})
    else:
        return render(request, "add_client.html", {"form": ClientForm})


def get(request):
    if request.method == 'GET':
        q_set = Client.objects.values()
        response = ClientForm.get(request, q_set)
    return render(request, "get_client.html", {'data': response})
