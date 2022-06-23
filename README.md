![example workflow](https://github.com/Densaur/docs/actions/workflows/api_yamdb.yml/badge.svg)



YAMDB_FINAL
http://51.250.104.86/admin

API для получения информации и обсуждения наиболее интересных произведений

Стэк технологий:
Python
Django Rest Framework
Postgres
Docker

Автор: Денис Клишин.
https://github.com/Densaur

Документация и возможности API:
К проекту подключен redoc. Для просмотра документации используйте эндпойнт redoc/

Развертывание:
Склонируйте репозитрий на свой компьютер
Создайте .env файл в директории infra/, в котором должны содержаться следующие переменные:
DB_ENGINE=django.db.backends.postgresql
DB_NAME= # название БД\ POSTGRES_USER= # ваше имя пользователя
POSTGRES_PASSWORD= # пароль для доступа к БД
DB_HOST=db
DB_PORT=5432\

Из папки infra/ соберите образ при помощи docker-compose $ docker-compose up -d --build
Примените миграции $ docker-compose exec web python manage.py migrate
Соберите статику $ docker-compose exec web python manage.py collectstatic --no-input
Для доступа к админке не забудьте создать суперюзера $ docker-compose exec web python manage.py createsuperuser