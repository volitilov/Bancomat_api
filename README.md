# Bankomat

[![Foo](https://img.shields.io/pypi/pyversions/Bankomat.svg)](https://pypi.python.org/pypi/Bankomat/)
[![Foo](https://travis-ci.org/volitilov/Bancomat_api.svg?branch=master)](https://travis-ci.org/volitilov/Bancomat_api)

----------------


API для банкомата. Тестовое задание в smartup school на backend.


### Requirements

`PostgreSQL 9.5`
На данный момент проверена работа, только с данной базой


### Install

```bash
$ pip install bankomat
```


### Usage

Инициализируте приложение
```bash
$ bankomat init
```

Создайте файл `.env` и запешите в него следующие данные:

```txt
SECRET_KEY='your_longSecret__:::key'

DATABASE_NAME='database_name'
DATABASE_USER='database_user'
DATABASE_PASSWORD='password'
DATABASE_HOST='host'
DATABASE_PORT='port'
```

В настройках конфигурации приложения включите окружение:

```python
PRODUCTION = True
```

Запуск приложения
```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```


### API

`/api/bank/set`
задает какое кол-во банкнот, которое есть в банкомате example:

```javascript
{
    "100": "50",
    "500": "25",
    "10": "50"
}
```

`/api/bank/withdraw`
снимает деньги example:

```javascript
{
    "amount": "5000"
}
```

`/api/bank/status`
отдает какие банкноты есть и сколько их в банкомате.