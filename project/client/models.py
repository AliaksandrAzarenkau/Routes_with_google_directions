from django.db import models


class Client(models.Model):
    organisation_name = models.CharField(max_length=50, help_text='Наименование клиента')
    phone_number = models.CharField(max_length=11, blank=True, help_text='Номер телефона')
    country = models.CharField(max_length=50, help_text='Страна')
    city = models.CharField(max_length=50, help_text='Город')
    street = models.CharField(max_length=50, help_text='Улица')
    building = models.CharField(max_length=5, help_text='Дом/строение')
    geolocation = models.CharField(max_length=20, blank=True, help_text='Координаты')
