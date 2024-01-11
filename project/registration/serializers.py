from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериализация при регистрации"""
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True,
                                     label='Пароль'
                                     )
    token = serializers.CharField(max_length=255, read_only=True, label='Токен')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        """Создание нового пользователя"""
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, label='Почта')
    username = serializers.CharField(max_length=255, read_only=True, label='Имя пользователя')
    password = serializers.CharField(max_length=128, write_only=True, label='Пароль')
    token = serializers.CharField(max_length=255, read_only=True, label='Токен')

    def validate(self, data):
        """Проверка валидности"""
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('Необходимо ввести адрес почты')

        if password is None:
            raise serializers.ValidationError('Пароль необходим для авторизации')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('Ошибка авторизации')

        if not user.is_active:
            raise serializers.ValidationError('Пользователь неактивен')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """Сериализация/десериализация объектов User"""
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True,
                                     label='Пароль'
                                     )

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'token',
            )

        read_only_fields = 'token'

    def update(self, instance, validated_data):
        """Обновление User"""
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
