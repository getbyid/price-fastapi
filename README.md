FastAPI + SQLModel + Alembic
============================

Применяются: FastAPI, async SQLAlchemy, SQLModel, SQLite, Alembic

```sh
$ pip install fastapi uvicorn sqlmodel aiosqlite alembic
```

## Запуск

```sh
$ uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8080
```

Swagger UI:
http://127.0.0.1:8080/docs

## Применение

Добавить товар:

```sh
$ curl -H "Content-Type: application/json" \
-d '{"category":"видеокарта","name":"Gigabyte GeForce GTX 1660 OC [GV-N1660OC-6GD]"}' \
http://localhost:8080/product
```

Добавить предложение (ссылку на товар в конкретном магазине):

```sh
$ curl -H "Content-Type: application/json" \
-d '{"product_id":1,"url":"https://www.dns-shop.ru/product/38d7d1eb43d73332/videokarta-gigabyte-geforce-gtx-1660-oc-gv-n1660oc-6gd/"}' \
http://localhost:8080/offer

$ curl -H "Content-Type: application/json" \
-d '{"product_id":1,"url":"https://www.wildberries.ru/catalog/8018513/detail.aspx"}' \
http://localhost:8080/offer
```

Получить все цены:

```sh
$ curl http://localhost:8080/history
```

Запустить обновление цен:

```sh
$ curl http://localhost:8080/update
```

## Парсеры

Применяются: HTTPX, lxml, cssselect

```sh
$ pip install httpx lxml cssselect
```

Не применяются:

* fake-useragent - требует setuptools
* beautifulsoup4 - много лишнего

Для парсеров есть тесты:

```sh
$ python -m pytest tests
```

## Полезные статьи

https://testdriven.io/blog/fastapi-sqlmodel/

https://docs.sqlalchemy.org/en/14/index.html
