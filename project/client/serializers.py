from rest_framework import serializers
from rest_framework.decorators import api_view

from .models import Client, ClientObjectsProfile


class ClientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['organisation_name', 'phone']

    def create(self, validated_data):
        """Создание клиента"""
        return Client.objects.crete(**validated_data)

    def update(self, instance, validated_data):
        """Обновление данных клиента"""
        instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
        instance.phone = validated_data.get('phone', instance.phone)
        return instance


class ClientObjectsProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientObjectsProfile
        fields = '__all__'

    def create(self, validated_data):
        """Создание карточки клиента"""
        return Client.objects.crete(**validated_data)

    def update(self, instance, validated_data):
        """Обновление карточки клиента"""
        instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.building = validated_data.get('building', instance.building)
        instance.geolocation = validated_data.get('geolocation', instance.geolocation)
        return instance
