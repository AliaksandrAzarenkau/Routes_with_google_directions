from django import forms

from .models import Client


class ClientForm(forms.Form):
    organisation_name = forms.CharField(required=True, label='Клиент')
    phone_number = forms.CharField(label='Контактный номер')
    country = forms.CharField(required=True, label='Страна')
    city = forms.CharField(required=True, label='Город')
    street = forms.CharField(required=True, label='Улица')
    building = forms.CharField(required=True, label='Дом/строение')
    geolocation = forms.CharField(label='Координаты')

    class Meta:
        model = Client
        fields = ('organisation_name',
                  'phone_number',
                  'country',
                  'city',
                  'street',
                  'building',
                  'geolocation',
                  )

# Добавление клиента
    def post(self, request):
        Client.objects.create(
            organisation_name=request.get('organisation_name'),
            phone_number=request.get('phone_number'),
            country=request.get('country'),
            city=request.get('city'),
            street=request.get('street'),
            building=request.get('building'),
            geolocation=request.get('geolocation'),
        )

# Получение списка всех клиентов
    def get_all(self, request):
        response = {}
        for values in request:
            if type(values) == dict:
                # Выводим список всех клиентов в словарь в формате:
                # {id клиента: {вся информация из модели Client по id}}
                response[values.get('id')] = values
        return response
