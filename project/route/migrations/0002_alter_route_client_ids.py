# Generated by Django 4.2.9 on 2024-01-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='client_ids',
            field=models.CharField(blank=True, max_length=255, verbose_name='Список ID объектов'),
        ),
    ]