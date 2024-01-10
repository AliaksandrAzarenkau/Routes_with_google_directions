from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    MANAGER = 'mngr',
    EMPLOYEE = 'empl',


class User(AbstractUser):
    position = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    role = models.CharField(
        max_length=4,
        choices=UserRole.choices, default=UserRole.EMPLOYEE,
        verbose_name='Права'
    )
    profile_photo = models.ImageField(
        blank=True,
        upload_to='.r/registration/profile_images/',
        height_field=None, width_field=None,
        max_length=100,
        verbose_name='Фото профиля'
    )
    date_joined = models.DateTimeField(auto_now=True)
