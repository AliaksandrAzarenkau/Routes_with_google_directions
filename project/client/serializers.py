from rest_framework import serializers

from .models import Client, ClientObjectsProfile
from .services import get_latlon


class ClientCreateSerializer(serializers.ModelSerializer):
    organisation_name = serializers.CharField(
        max_length=50,
        required=True,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "Обязательно для заполнения",
            "blank": "Название организации необходимо",
        },
        label='Наименование клиента*'
    )
    phone = serializers.CharField(
        max_length=11,
        required=True,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "Обязательно для заполнения",
            "blank": "Номер телефона необходим",
        },
        label='Номер телефона*'
    )

    # def update(self, instance, validated_data):
    #     """Обновление данных клиента"""
    #     instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     return instance

    class Meta:
        model = Client
        fields = ['organisation_name', 'phone']


class ClientObjectsProfileSerializer(serializers.ModelSerializer):

    def create(self, request_data):
        """Создание карточки клиента"""
        country = request_data.get('country'),
        city = request_data.get('city'),
        street = request_data.get('street'),
        building = request_data.get('building'),
        latlon = get_latlon([country, city, street, building])

        response = ClientObjectsProfile.objects.create(
            organisation_name=request_data.get('organisation_name'),
            phone=request_data.get('phone'),
            country=country[0],
            city=city[0],
            street=street[0],
            building=building[0],
            lat=latlon[0],
            lon=latlon[1]
        )
        return response

    # def update(self, instance, validated_data):
    #     """Обновление карточки клиента"""
    #     instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.street = validated_data.get('street', instance.street)
    #     instance.building = validated_data.get('building', instance.building)
    #     instance.geolocation = validated_data.get('geolocation', instance.geolocation)
    #     return instance

    class Meta:
        model = ClientObjectsProfile
        fields = [
            'organisation_name',
            'phone',
            'country',
            'city',
            'street',
            'building'
        ]


class ClientListSerializer(serializers.Serializer):
    organisation_name = serializers.CharField(
        max_length=50,
        required=True,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "on",
            "required": True,
        },
        error_messages={
            "required": "Обязательно для заполнения",
            "blank": "Название организации необходимо",
        },
        label='Наименование клиента*'
    )
    phone = serializers.CharField(
        max_length=11,
        required=True,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "on",
            "required": True,
        },
        error_messages={
            "required": "Обязательно для заполнения",
            "blank": "Номер телефона необходим",
        },
        label='Номер телефона*'
    )

    def get_clients(self):
        """Список всех клиентов"""
        clients_set = Client.objects.all()

        return clients_set

    def get_objects(self, pk, ids=None):
        """Для PK: Список всех объектов одного клиента
        Для IDS: данные клиент-объект для маршрута"""
        if pk:
            resp = {'client_name': Client.objects.get(id=pk),
                    'client_obj': ClientObjectsProfile.objects.filter(organisation_name_id=pk)}

        elif ids:
            client_names = []
            client_objects = []
            for object_id in ids:
                obj = ClientObjectsProfile.objects.get(id=object_id)
                client_objects.append(obj)
                client_id = obj.organisation_name_id
                client = Client.objects.get(id=client_id)
                client_names.append(client)

            resp = {'client_names': client_names,
                    'client_obj': client_objects}

        return resp

    class Meta:
        model = Client
        fields_client = ['organisation_name', 'phone']
