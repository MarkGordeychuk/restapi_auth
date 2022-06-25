# Restapi_auth - *тестовое задание для Backend-разработчиков платформы ДРУГ*
### Необходимо:
- Python
- PostgreSQL
#### или
- Docker
## Как запустить?
1. Клонируйте или скачайте проект.
2. Смените директорию на ```restapi_auth```
3. Создайте виртуальную среду: ```python -m venv venv```
4. Активируйте виртуальную среду: ОС Mac и Linux: ```source venv/bin/activate```, ОС Windows: ```venv\scripts\activate```
5. Установите зависимости: ```pip install -r requirements.txt```
6. Создайте файл ```.env``` с переменными окружения, который должен содержать в себе следующие значения:
- ```DJANGO_DEBUG=0/1``` - включить режим отладки (по умолчанию ```1```)
- ```DJANGO_SECRET_KEY``` - секретный ключ
- ```DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost``` - список разрешённых хостов
- ```POSTGRES_HOST=localhost``` - хост БД (по умолчанию ```localhost```)
- ```POSTGRES_DB``` - имя БД
- ```POSTGRES_USER``` - пользователь БД
- ```POSTGRES_PASSWORD``` - пароль БД
7. Запустите PostgreSQL.
8. Совершите миграцию базы данных: ```python manage.py migrate```
9. При необходимости создайте супер-пользователя: ```python manage.py createsuperuser```
10. Запустите сервер: ```python manage.py runserver 8080```
11. Теперь вы сможете открыть этот адрес: http://127.0.0.1:8080/
## Как запустить с помощью Docker?
1. Клонируйте или скачайте проект.
2. Смените директорию на ```restapi_auth```
3. Создайте файл ```.env``` с переменными окружения, который должен содержать в себе следующие значения:
- ```DJANGO_DEBUG=0/1``` - включить режим отладки (по умолчанию ```1```)
- ```DJANGO_SECRET_KEY``` - секретный ключ
- ```DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost``` - список разрешённых хостов
- ```POSTGRES_DB``` - имя БД
- ```POSTGRES_USER``` - пользователь БД
- ```POSTGRES_PASSWORD``` - пароль БД
4. Создайте образ: ```docker-compose build```
5. Запустите базу данных ```docker-compose up -d db``` и немного подождите
6. Запустите web-сервер ```docker-compose up -d web```
7. Совершите миграцию базы данных: ```docker-compose exec web python manage.py migrate```
8. При необходимости создайте супер-пользователя: ```docker-compose exec web python manage.py createsuperuser```
9. Теперь вы сможете открыть этот адрес: http://127.0.0.1:8080/