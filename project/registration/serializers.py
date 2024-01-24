from rest_framework import serializers

from .models import User, UserProfilePhoto


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True, label='ID')
    first_name = serializers.CharField(label='Имя')
    last_name = serializers.CharField(label='Фамилия')
    email = serializers.CharField(label='Почта')
    password = serializers.CharField(write_only=True, label='Пароль')
    position = serializers.CharField(label='Должность')
    profile_photo = serializers.ImageField(label='Фото профиля')

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            position=validated_data.get('position'),
            profile_photo=validated_data.get('profile_photo')
        )

        return user


class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(label='Имя',
                                       style={
                                           "input_type": "text",
                                           "autofocus": False,
                                           "autocomplete": "off",
                                           "required": True,
                                       },
                                       error_messages={
                                           "required": "Обязательно для заполнения",
                                           "blank": "Укажите имя",
                                       }
                                       )
    last_name = serializers.CharField(label='Фамилия',
                                      style={
                                          "input_type": "text",
                                          "autofocus": False,
                                          "autocomplete": "off",
                                          "required": True,
                                      },
                                      error_messages={
                                          "required": "Обязательно для заполнения",
                                          "blank": "Укажите фамилию",
                                      }
                                      )
    email = serializers.CharField(label='Почта',
                                  style={
                                      "input_type": "text",
                                      "autofocus": False,
                                      "autocomplete": "off",
                                      "required": True,
                                  },
                                  error_messages={
                                      "required": "Обязательно для заполнения",
                                      "blank": "Укажите почту",
                                  }
                                  )
    password = serializers.CharField(label='Пароль',
                                     write_only=True,
                                     style={
                                         "input_type": "text",
                                         "autofocus": False,
                                         "autocomplete": "off",
                                         "required": True,
                                     },
                                     error_messages={
                                         "required": "Обязательно для заполнения",
                                         "blank": "Укажите пароль",
                                     }
                                     )
    position = serializers.CharField(label='Должность',
                                     style={
                                         "input_type": "text",
                                         "autofocus": False,
                                         "autocomplete": "off",
                                         "required": True,
                                     },
                                     error_messages={
                                         "required": "Обязательно для заполнения",
                                         "blank": "Укажите должность",
                                     }
                                     )

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            position=validated_data.get('position'),
        )

        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'position']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label='Адрес электронной почты',
                                  style={
                                      "input_type": "text",
                                      "autofocus": False,
                                      "autocomplete": "off",
                                      "required": True,
                                  },
                                  error_messages={
                                      "required": "Обязательно для заполнения",
                                      "blank": "Почта необходима",
                                  },
                                  )
    password = serializers.CharField(write_only=True,
                                     style={
                                         "input_type": "text",
                                         "autofocus": False,
                                         "autocomplete": "off",
                                         "required": True,
                                     },
                                     error_messages={
                                         "required": "Обязательно для заполнения",
                                         "blank": "Пароль обязателен",
                                     },
                                     label='Пароль')

    class Meta:
        model = User
        fields = ['email', 'password']


class UserEditProfileSerializer(serializers.Serializer):
    model = User

    email = serializers.CharField(label='Почта',
                                  style={
                                      "input_type": "text",
                                      "autofocus": False,
                                      "autocomplete": "on",
                                      "required": True,
                                  },
                                  error_messages={
                                      "required": "Обязательно для заполнения",
                                      "blank": "Укажите почту",
                                  }
                                  )
    first_name = serializers.CharField(label='Имя',
                                       style={
                                           "input_type": "text",
                                           "autofocus": False,
                                           "autocomplete": "on",
                                           "required": True,
                                       },
                                       error_messages={
                                           "required": "Обязательно для заполнения",
                                           "blank": "Укажите имя",
                                       }
                                       )
    last_name = serializers.CharField(label='Фамилия',
                                      style={
                                          "input_type": "text",
                                          "autofocus": False,
                                          "autocomplete": "on",
                                          "required": True,
                                      },
                                      error_messages={
                                          "required": "Обязательно для заполнения",
                                          "blank": "Укажите фамилию",
                                      }
                                      )
    position = serializers.CharField(label='Должность',
                                     style={
                                         "input_type": "text",
                                         "autofocus": False,
                                         "autocomplete": "on",
                                         "required": True,
                                     },
                                     error_messages={
                                         "required": "Обязательно для заполнения",
                                         "blank": "Укажите должность",
                                     }
                                     )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'position']


class UserPhotoProfileSerializer(serializers.Serializer):
    model = UserProfilePhoto

    profile_photo = serializers.ImageField(label='Фото профиля',
                                           style={
                                               "input_type": "text",
                                               "autofocus": False,
                                               "autocomplete": "on",
                                               "required": False,
                                           },
                                           error_messages={
                                               "required": "Неверный формат изображения",
                                               "blank": "Фото профиля",
                                           }
                                           )

    def update(self, instance, validated_data):
        instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
        instance.save()
        return instance

    class Meta:
        model = UserProfilePhoto
        fields = ['profile_photo']
