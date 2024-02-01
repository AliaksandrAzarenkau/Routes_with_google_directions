from rest_framework import serializers

from .models import Route

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductSerializer(serializers.Serializer):
    quantity = serializers.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    update = serializers.BooleanField(required=False, initial=False)


class RouteCreateSerializer(serializers.Serializer):

    def create(self, validated_data):
        print(validated_data.get('email'))
        print(validated_data.get('client_ids'))
        response = Route.objects.create(
            email=validated_data.get('email'),
            client_ids=validated_data.get('client_ids'),
        )

        return response

    class Meta:
        model = 'Route'
        fields = ['email', 'client_ids', 'created']
