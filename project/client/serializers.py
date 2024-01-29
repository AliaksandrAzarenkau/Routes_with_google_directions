from rest_framework import serializers

from .models import Client, ClientObjectsProfile


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

    # def create(self, request_data):
    #     """Создание клиента"""
    #     response = Client.objects.create(
    #         organisation_name=request_data.get('organisation_name'),
    #         phone=request_data.get('phone')
    #     )
    #     return response

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
        response = ClientObjectsProfile.objects.create(
            organisation_name=request_data.get('organisation_name'),
            phone=request_data.get('phone'),
            country=request_data.get('country'),
            city=request_data.get('city'),
            street=request_data.get('street'),
            building=request_data.get('building'),
            geolocation=request_data.get('geolocation'),
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
        fields = '__all__'


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

    def get_objects(self, pk):
        """Список всех объектов одного клиента"""
        resp = {'client_name': Client.objects.get(id=pk),
                'client_obj': ClientObjectsProfile.objects.filter(organisation_name_id=pk)}

        return resp

    class Meta:
        model = Client
        fields_client = ['organisation_name', 'phone']

