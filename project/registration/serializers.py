from rest_framework import serializers

from .models import User


class UserResponseHandling:
    username = serializers.CharField(required=True, label='Login')
    password = serializers.CharField(required=True, label='Пароль')
    first_name = serializers.CharField(required=True, label='Имя')
    last_name = serializers.CharField(required=True, label='Фамилия')
    email = serializers.EmailField(label='Почта')
    position = serializers.CharField(label='Должность')
    role = serializers.CharField(required=True, label='Права')
    profile_photo = serializers.ImageField(label='Фото профиля')


class UserCreateSerializer(UserResponseHandling, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'position',
                  'role',
                  'profile_photo'
                  )

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data, partial=True):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
        instance.save(update_fields=['password', 'first_name', 'last_name', 'email', 'profile_photo'])
        return instance
