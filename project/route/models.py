from django.db import models

from registration.models import User
from client.models import Client


# class Cart(models.Model):
#     email = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
#     organisation_name = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='Контрагент')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания маршрута')

class Route(models.Model):
    email = models.CharField(max_length=255, blank=True, verbose_name='Пользователь')
    client_ids = models.CharField(max_length=255, blank=True, verbose_name="Список ID объектов")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания маршрута')
