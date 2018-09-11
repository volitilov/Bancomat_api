# Bancomat_api

API для банкомата для. Тестовое задание в smartup school на backend.

### API

`/api/bank/set` - задает какое кол-во банкнот, которое есть в банкомате.
example:
```javascript
{
    "100": "50",
    "500": "25",
    "10": "50"
}
```

`/api/bank/withdraw` - снимает деньги. 
example:
```javascript
{
    "amount": "5000"
}
```

`/api/bank/status` - отдает какие банкноты есть и сколько их в банкомате.
