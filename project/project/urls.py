from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    # path('client/', include('client.urls')),
    # path('route/', include('route.urls')),
]
