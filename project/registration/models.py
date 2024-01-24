from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import models as auth_models


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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class UserProfilePhoto(models.Model):
    email = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Почта')
    profile_photo = models.ImageField(
        upload_to='./registration/static/profile_images',
        default='./registration/static/profile_images/profile_picture_icon.png',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))],
        verbose_name='Фото профиля'
    )
