from django.contrib import admin

from client.models import Client, ClientObjectsProfile


admin.site.register([Client, ClientObjectsProfile])
