# Пример реализации шаблона "Декоратор"

**Исходный код**: ./Src/.. <br>
**Модульные тесты**: ./Tst/..

### Задания
1. Доработать класс `receipe`. Добавить проверки:
	- При добавлении `базовой номенеклатуры` запретить добавление с типами:  `Товар`, `Ингредиент`
	- При добавлении `ингредиента` в состав, запретить добавление с типами: `Товар`
2. Доработать модульные тесты. Добавить варианты с проверкой исключений
```
  if nomenclature is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(nomenclature,  reference):
            raise Exception("Некорректный тип данных!")
        
        if self._nomenclature.id == nomenclature.id:
            raise Exception("Невозможно добавить в состав номенклатуру совпадающую с основной номенклатурой!")
        
        items = list(filter(lambda x: x == nomenclature.id, self._ingrediens.keys()))
        if len(items) != 0:
            raise Exception("Указанная номенклатура уже включена в состав!") 
```	
3. Добавить модульный тест с эмитацией включение одного рецепта в другой. При выполнении данного модульного теста добавить
текстовое описание. Пример:
```
Номенклатура 1
	Состав:
		- Номенклатура 2
		- Номенклатура 3
		- Номенклатура 4
			Состав:
				- Номенклатура 5
		- Номенклатура 7		
```
4. Добавить новый конвертор `receipe` -> Json (на основе: [convertor_to_json](https://github.com/VolovikovAlexander/Patterns/blob/main/Step8/Src/Logics/convertor_to_json.py)
5. Разработать новый класс `receipe_factory` на основе шаблона [Фабрика](https://github.com/VolovikovAlexander/Patterns/blob/main/Step6/readme.md)
Пример: https://github.com/VolovikovAlexander/Patterns/blob/main/Step8/Src/Logics/nomenclature_factory.py
6. Добавить генерацию и хранение рецептов в класс `data_factory`
 

#### Опционально
- Создать документ с техническим описанием в формате `Markdown`. 
В документе описать примеры. Дать краткое описание данной части проекта. 





