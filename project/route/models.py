from django.db import models
from django.urls import reverse


class Route(models.Model):
    email = models.CharField(max_length=255, blank=True, verbose_name='Пользователь')
    client_ids = models.CharField(max_length=255, verbose_name="Список ID объектов")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания маршрута')

    def get_absolute_url(self):
        return reverse('date_archive', kwargs={'pk': self.id})
