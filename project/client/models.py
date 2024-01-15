from django.db import models


class Client(models.Model):
    organisation_name = models.CharField(max_length=50, verbose_name='Наименование клиента')
    phone = models.CharField(max_length=11, blank=True, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')


class ClientObjectsProfile(models.Model):
    organisation_name = models.ForeignKey(
                                          Client,
                                          on_delete=models.CASCADE,
                                          max_length=50,
                                          verbose_name='Наименование клиента'
                                         )
    phone = models.CharField(max_length=11, blank=True, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    building = models.CharField(max_length=5, verbose_name='Дом/строение')
    geolocation = models.CharField(max_length=20, blank=True, verbose_name='Координаты')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')
