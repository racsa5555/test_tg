### Тестовое задание

## Запуск проекта

1. Создайте файл .env(пример env_example)

2. Создайте виртуальное окружение

`python3 -m venv venv`

3. Скачайте необходимые зависимости 

`pip install -r requirements.txt`

4. Создайте Базу данных в postgresql

`psql postgres`

`create database <название>`

5. Запустите файл models.py(для создания таблицы в БД)

`cd app`

`python3 models.py`

6. Запустите файл main.py

`python3 main.py`