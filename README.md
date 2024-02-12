# О проекте:
Проект представляет собой сайт, упрощающий логистические задачи по доставке грузов.
В проекте реализована система хранения базы клиентов, с возможностью добавления новых. Так же реализовона возможность построение оптимального маршрута между точками доставки(клиентами).
Проект написан на фреймворке Django REST с использованием Google Directions API и Google Maps JavaScript API.

## Установка и запуск
Для запуска понадобится:
1. Скопировать файлы проекта из репозитория
2. Установить все необходимые библиотеки коммандой:
   
   ```
   pip install -r requirements.txt
   ```
3. Скопировать свои ключи Django-проекта и Google API в файл .env
4. Запустить локальный сервер коммандой:

   ```
   python manage.py runserver
   ```
Сайт будет доступен по адресу <http://127.0.0.1:8000/>

