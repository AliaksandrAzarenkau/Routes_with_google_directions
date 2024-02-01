from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view()),
    path('route/', include('route.urls')),
    path('registration/', include('registration.urls')),
    path('client/', include('client.urls')),
]
