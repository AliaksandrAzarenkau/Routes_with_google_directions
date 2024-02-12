from rest_framework import serializers

from route.models import Route
from client.models import ClientObjectsProfile

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductSerializer(serializers.Serializer):
    quantity = serializers.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    update = serializers.BooleanField(required=False, initial=False)


class RouteCreateSerializer(serializers.Serializer):

    def create(self, validated_data):
        response = Route.objects.create(
            email=validated_data.get('email'),
            client_ids=validated_data.get('client_ids'),
        )

        return response

    class Meta:
        model = 'Route'
        fields = ['email', 'client_ids', 'created']


class RouteArchiveSerializer(serializers.Serializer):
    email = serializers.CharField(label='Пользователь')
    client_ids = serializers.CharField(label="Список ID объектов")
    created = serializers.DateTimeField(label='Дата создания маршрута')

    def get_details(self, pk):
        """Достаём все адреса объектов маршрута"""
        route = Route.objects.get(id=pk)
        ids = route.client_ids

        objects_list = []
        filtered_ids = ids.split(',')
        for i in filtered_ids:
            obj = ClientObjectsProfile.objects.get(id=int(i))
            objects_list.append(obj)

        return objects_list

    class Meta:
        model = Route
        fields = ['email', 'client_ids', 'created']
