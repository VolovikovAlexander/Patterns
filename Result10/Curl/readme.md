# Интеграционное тестирование
Вариант `Curl`


1. Получить список номенклатуры
```
curl http://127.0.0.1:5000/api/nomenclature
```

2. Получить конкретную номенклатуру
```
curl http://127.0.0.1:5000/api/nomenclature?id=cdbbecb3fa594a799e5b4c6a14058c42
```

3. Получить значение периода блокировки
```
curl http://127.0.0.1:5000/api/block_period
```

4. Изменить блокирующий период
```
curl http://127.0.0.1:5000/api/block_period?period=2022-01-01
```

5. Получить текущие обороты
```
curl http://127.0.0.1:5000/api/storage/turns?start_period=1900-01-01&stop_period=2025-01-01
```
