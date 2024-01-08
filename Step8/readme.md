# Пример реализации шаблона "Общие данные" 
> на основе `Rest`

**Исходный код**: ./Src/.. <br>
**Модульные тесты**: ./Tst/..

### Установка
1. Установка виртуального окружения
```bash
sudo apt install python3.10-venv
python3 -m venv .venv
. .venv/bin/activate
```

2. Установить Flask
```bash
pip3 install -U connexion[flask]
pip3 install -U connexion[swagger-ui]
pip3 install -U connexion[uvicorn]
pip3 install -U flask-restplus
pip3 install -U Flask
```

3. Запуск: http://127.0.0.1:8000/api/ui/

### Задания
1. Добавить в swagger остальные методы: `get_nomenclature_groups`, `get_nomenclature_units`
2. Добавить в swagger новые методы: [`получить историю операций`](https://github.com/VolovikovAlexander/Patterns/blob/main/Step8/Src/Models/nomenclature_history.py), [`получить баланс`](https://github.com/VolovikovAlexander/Patterns/blob/main/Step8/Src/Models/nomenclature_balance.py). 
Метод должен работать с конкретным кодом номенклатуры.
Пример: 
https://github.com/VolovikovAlexander/Studies/blob/main/Yandex.Cloud/Main.py#L15



#### Опционально
- Создать документ с техническим описанием в формате `Markdown`. 
В документе описать примеры. Дать краткое описание данной части проекта. 





