# DjangoChatRoom
**Django chat c 2-мя типами чатов:**
1. http://127.0.0.1:8000 на XMLHttpRequest запросах с интервалом 1 секунду 
2. http://127.0.0.1:8000/choose на WebSocket

Кроме того, добавлен DRF, который позволяет отправлять сообщение по REST API:
- Страница API доступна по адресу http://127.0.0.1:8000/api
- Описание по адресу http://127.0.0.1:8000/swagger-ui

Для работы проекта нужно установить:
```
pip install django
pip install djangorestframework
pip install -U channels["daphne"]

```
