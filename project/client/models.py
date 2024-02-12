from django.db import models
from django.urls import reverse


class Client(models.Model):
    organisation_name = models.CharField(max_length=50, verbose_name='Наименование клиента')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')

    def get_organisation_name(self):
        return self.organisation_name

    def get_absolute_url(self):
        return reverse('objects', kwargs={'pk': self.id})


class ClientObjectsProfile(models.Model):
    organisation_name = models.ForeignKey(
                                          Client,
                                          on_delete=models.DO_NOTHING,
                                          max_length=50,
                                          verbose_name='Наименование клиента'
                                         )
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    building = models.CharField(max_length=5, verbose_name='Дом/строение')
    lat = models.CharField(max_length=20, default=None, verbose_name='Широта')
    lon = models.CharField(max_length=20, default=None, verbose_name='Долгота')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')

    def get_phone(self):
        return self.phone

    def get_address(self):
        address = {
            'country': self.country,
            'city': self.city,
            'street': self.street,
            'building': self.building
        }
        return address
