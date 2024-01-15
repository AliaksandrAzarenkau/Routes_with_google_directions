from django.contrib import admin

from .models import Client, ClientObjectsProfile


admin.site.register([Client, ClientObjectsProfile])
