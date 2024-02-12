from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=50, verbose_name='Наименование клиента')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')),
            ],
        ),
        migrations.CreateModel(
            name='ClientObjectsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('building', models.CharField(max_length=5, verbose_name='Дом/строение')),
                ('geolocation', models.CharField(blank=True, max_length=20, verbose_name='Координаты')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления данных')),
                ('organisation_name', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.DO_NOTHING, to='client.client', verbose_name='Наименование клиента')),
            ],
        ),
    ]
