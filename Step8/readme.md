# Занятие № 8
**Десериализация**

Цель:
- Закрепить опыт работы с ООП.
- Закрепить опыт работы с `рекурсией`
- Закрепить опыт работы с системой `swagger`
- Продемонстрировать работу с системной библиотекой `json`
- Закрепить опыт работы с шаблоном `Фабрика`

## Выполнить
* Доработать классы для конвертации:
	- `dict` в `datetime`
	- `dict` в `int`
	- `dict` в `str`
* Доработать класс наследник от `abstact_convertor`. Реализовать десериализацию из словаря в стуктуру доменных данных
  с использованием шаблона **Фабрика**
* Добавить модульные тесты. Выполнить `сериализацию` и `десериализация`. Сравнить полученные данные.
 

## Задание
1. Необходимо доработать механизм десериализации данных в формате `Json`, `XML`
2. Создать несколько тестовых произвольных файлов в формате `Json`,`XML` 
   с данными `Еиница измерения`
3. Написать модульный тест который загрузит данные из файлов в текущие доменные модели.
4. Добавить точки выполнения в RestApi:
	- `PUT` Добавить новую единицу измерения (`Json`)
	- `PATCH` Изменить параметры единицы измерения (`Json`)
	- `PUT` Добавить новую номенклатуру (`Json`)
	- `PATCH` Изменить параметры номенклатуры (`Json`)
 

