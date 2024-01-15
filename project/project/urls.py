from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/', include('client.urls')),
    path('api/registration/', include('registration.urls')),
]
