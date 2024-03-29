# Generated by Django 5.0.1 on 2024-01-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_user_avatar_remove_user_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='./registration/profile_images/', verbose_name='Фото профиля'),
        ),
    ]
