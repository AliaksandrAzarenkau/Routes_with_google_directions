from django.shortcuts import render, redirect

from .forms import ClientForm


def create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.post(request.POST)

            """Поправить редирект"""

            return redirect('/')
        else:
            return render(request, "client.html", {"form": ClientForm})
    else:
        return render(request, "client.html", {"form": ClientForm})
