# Занятие № 1
**Настройки**

Цель:
- Познакомить слушателей курса с шаблоном `Одиночка` на примере работы с настройками приложения.
- Обучить слушателей использовать приемы ООП при проектировании приложений.

## Выполнить:
* Создаем структуру проекта.
* Создаем первую модель данных : `settings_model`
* Создаем первую логическую структуру : `settings_manager`
* Создаем первый модульный на проверку работы `settings_manager` 

## Задание
Необходимо:
1. Доработать класс `settings_manager`. 
	- Добавить  / изменить метод `convert`. 
	- Данный метод должен формировать объект от класса `settings_manager` из загруженного словаря.
2. Добавить модульный тест, который проверяет загрузку данных в объект от класса `settings_manager`. Проверить загрузку всех свойств.
3. Доработать класс `settings_manager`. 
	- Сделать универсальную загрузку из файла, который может располагаться в любом каталоге.
4. Добавить модульный тест который проверит загрузку настроек из файла в другом каталоге и другого наименования.
5. Доработать класс `settings_model` добавить следующие ограничения:
	- `ИНН` : 12 симв
	- `Счет` 11 симв
	- `Корреспондентский счет` 11 симв
 	- `БИК` 9 симв
	- `Наименование`
	- `Вид собственности` 5 симв



