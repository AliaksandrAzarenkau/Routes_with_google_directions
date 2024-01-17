from django.db import models
from django.contrib.auth import models as auth_models
import jwt
from datetime import datetime, timedelta
from django.conf import settings


class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, first_name, last_name, is_staff=False, is_superuser=False, password=None):
        if not email:
            raise ValueError('Нужно указать адрес почты')

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='Почта')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    position = models.CharField(max_length=255, blank=True, verbose_name='Должность')
    profile_photo = models.ImageField(
        upload_to='./registration/static/profile_images',
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        verbose_name='Фото профиля'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

# class UserManager(BaseUserManager):
#
#     def create_user(self, username, email, password=None):
#         """Создаёт и возвращает пользователя с почтой и паролем"""
#         if username is None:
#             raise TypeError("Необходимо имя пользователя")
#
#         if email is None:
#             raise TypeError("Необходима почта пользователя")
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """Создаёт и возвращает суперпользователя с почтой и паролем"""
#         if password is None:
#             raise TypeError("Необходимо имя пользователя")
#
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         return user
#
#
# class User(AbstractUser, PermissionsMixin):
#     username = models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Имя пользователя')
#     email = models.EmailField(db_index=True, unique=True, verbose_name='Почта')
#     first_name = models.CharField(max_length=255, verbose_name='Имя')
#     last_name = models.CharField(db_index=True, max_length=255, verbose_name='Фамилия')
#     is_active = models.BooleanField(default=True, verbose_name="Состояние учётной записи")
#     is_staff = models.BooleanField(default=False, verbose_name="Администрация")
#     created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
#     updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')
#     avatar = models.ImageField(upload_to='./registration/profile_images/',
#                                height_field=None,
#                                width_field=None,
#                                max_length=100,
#                                blank=True,
#                                verbose_name='Фото профиля'
#                                )
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = UserManager()
#
#     def __str__(self):
#         """ Строковое представление модели (в консоли) """
#         return self.email
#
#     @property
#     def token(self):
#         """Позволяет получить токен пользователя путем вызова user.token"""
#         return self._generate_jwt_token()
#
#     def get_full_name(self):
#         """Возвращает имя и фамилию пользователя"""
#         full_name = f'{self.first_name} {self.last_name}'
#         return full_name
#
#     def get_short_name(self):
#         """Возвращает имя пользователя"""
#         return self.username
#
#     def _generate_jwt_token(self):
#         """Генерирует веб-токен JSON, в котором хранится идентификатор пользователя"""
#         dt = datetime.now() + timedelta(days=1)
#
#         token = jwt.encode({'id': self.pk, 'exp': int(dt.timestamp())}, settings.SECRET_KEY, algorithm='HS256')
#         return token.decode('utf-8')
