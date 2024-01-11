from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer


class RegistrationAPIVew(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """Регистрация пользователя"""
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """Логинизация пользователя"""
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        """Преобразование объекта User для последующего возврата"""
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """Обновление объекта User"""
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
