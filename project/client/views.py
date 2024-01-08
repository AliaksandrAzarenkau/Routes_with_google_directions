from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Client


# Добавление клиента
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


# Получение всех клиентов
def get_all(request):
    if request.method == 'GET':
        q_set = Client.objects.values()
        response = ClientForm.get_all(request, q_set)
    return render(request, "get_client.html", {'data': response})
