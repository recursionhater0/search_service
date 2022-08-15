# search_service
Тестовое задание. Сервис для асинхронного поиска данных о полетах в различных провайдерах

## Требования
1. Сервисы должен быть написан на языке Python с использованием любого из веб фреймворков 
2. В качестве хранилища данных можно использовать любую технологию.
3. Сервер должен быть доступен на порту 9000 
4. Предоставить инструкцию по запуску приложения. В идеале (но не обязательно) – использовать контейнеризацию с возможностью запустить проект командой docker-compose up

Note: Эндпоинта /api/v1/airflow/exchange_rate/ не было в ТЗ. Он был добавлен для тестирования запроса. Также в Dockerfile закоментирован entrypoint, иначе celery в контейнере не запускается.

## Installation

```bash
docker compose up --build
```

## URL
localhost:9000/api/v1/swagger/

## Screenshot
![alt text](https://github.com/RamazanPython/search_service/blob/master/screenshot.png)
