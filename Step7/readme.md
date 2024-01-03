# Пример реализации шаблона "Общие данные" 
> на основе `Rest`

**Исходный код**: ./Src/.. <br>
**Модульные тесты**: ./Tst/..

### Установка
1. Установка виртуального окружения
```
sudo apt install python3.10-venv
python3 -m venv .venv
. .venv/bin/activate
```

2. Установить Flask
```
pip3 install -U Flask
pip3 install flask-restplus
```

#### Задания
1. Доработать метод `to_dict` Исключить набор условий. Включить шаблон фабрика.
```
 def to_dict(source):
```
2. Доработать основной файл `main.py`. Добавить методы [Rest](https://ru.wikipedia.org/wiki/REST):
    - Список всех групп номенклатуры `group_nomenclature`
    - Список всех единиц измерения `unit_nomenclature`
    - Список всех историй изменения номенклатуры `nomenclature_history`
    - Баланс номенклатуры `nomenclature_balance`

3. Добавить в класс `app_settings` (настройки) новую настройку: количество номенклатуры.
    - Доработать основной файл `main.py`. Добавить количество объектов для генерации из настроек (setting.json)
    ```
    if __name__ == "__main__":
    data_factory.create_nomenclature(100)
    app.run(debug=True)
    ```   
4. Добавить метод [Rest](https://ru.wikipedia.org/wiki/REST) в основной файл для вывода текущий настроек (settings.json)
5. Написать клиента для подключения и загрузки данных [Rest](https://ru.wikipedia.org/wiki/REST).
Вывести список номенклатуры.

#### Опционально
    - Создать документ с техническим описанием в формате `Markdown`. 
	В документе описать примеры. Дать краткое описание данной части проекта. 





