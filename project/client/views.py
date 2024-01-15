from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .serializers import ClientCreateSerializer, ClientObjectsProfileSerializer


class ClientAPIVew(APIView):
    permission_classes = [AllowAny]
    serializer_class = ClientCreateSerializer

    def post(self, request):
        """Добавление данных клиента"""
        serializer_data = request.data.get('client', {})
        serializer = self.serializer_class(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request):
        """Обновление данных клиента"""
        serializer_data = request.data.get('client', {})
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientProfileAPIVew(APIView):
    permission_classes = [AllowAny]
    serializer_class = ClientObjectsProfileSerializer

    def post(self, request):
        """Добавление карточки клиента"""
        serializer_data = request.data.get('client', {})
        serializer = self.serializer_class(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request):
        """Обновление данных карточки клиента"""
        serializer_data = request.data.get('client', {})
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
