# Пример реализации абстрактного класса

**Исходный код**: ./Src/..<br>
**Модульные тесты**: ./Tst/..

#### Задания
1. Изменить код класса `error_proxy`. Заменить на абстрактный метод.
2. Добавить несколько наследников которые будут разные варианты `Exception` перехватывать
3. Добавить собственный класснаследник от `Exception` и реализовать обработку.
4. Всегда проверять и расширять модульные тесты 

Исходный метод
```
     def set_error(self, exception: Exception):
        " Записать текстовое описание ошибки по исключению"
        if exception  is None:
            self._error_text = ""
            
        self._error_text = "Ошибка! " + str(exception)    
```

#### Опционально
- Создать документ с техническим описанием в формате `Markdown`. 
В документе описать примеры. Дать краткое описание данной части проекта. 
