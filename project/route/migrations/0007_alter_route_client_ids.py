# Generated by Django 4.2.9 on 2024-02-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_alter_route_client_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='client_ids',
            field=models.CharField(max_length=255, verbose_name='Список ID объектов'),
        ),
    ]