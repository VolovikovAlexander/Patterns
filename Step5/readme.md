# Пример реализации шаблона "Клиент сервер"

**Исходный код**: ./Src/.. <br>
**Модульные тесты**: ./Tst/..

#### Инструменты
1. Установить [SQLBrowser](https://sqlitebrowser.org/)
2. Создать пустую базу данных. В ней таблицу:
```sql
CREATE TABLE "history" (
	"id"	INTEGER NOT NULL  ,
	"nomenclature_code"	TEXT NOT NULL,
	"turn"	INTEGER NOT NULL,
	"comments"	TEXT,
	"period"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```
3. Выполнить SQL запрос:
```sql
-- 9f1fed2c-926d-11ee-b9d1-0242ac120002
insert into history(nomenclature_code, turn,  comments,  period)
values('9f1fed2c-926d-11ee-b9d1-0242ac120002', 10, 'Начальный остаток','2023-10-01 00:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('9f1fed2c-926d-11ee-b9d1-0242ac120002', 5, 'Поступление','2023-10-02 00:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('9f1fed2c-926d-11ee-b9d1-0242ac120002', -2, 'Списание','2023-10-03 10:00');

-- 203be59a-926f-11ee-b9d1-0242ac120002
insert into history(nomenclature_code, turn,  comments,  period)
values('203be59a-926f-11ee-b9d1-0242ac120002', 0, 'Начальный остаток','2023-10-01 00:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('203be59a-926f-11ee-b9d1-0242ac120002', 20, 'Поступление','2023-11-02 15:00');

-- 53728856-926f-11ee-b9d1-0242ac120002
insert into history(nomenclature_code, turn,  comments,  period)
values('53728856-926f-11ee-b9d1-0242ac120002', 0, 'Начальный остаток','2023-10-01 00:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('53728856-926f-11ee-b9d1-0242ac120002', -5, 'Списание','2023-11-02 15:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('53728856-926f-11ee-b9d1-0242ac120002', 5, 'Поступление','2023-11-02 15:00');

-- 79c9f71e-926f-11ee-b9d1-0242ac120002
insert into history(nomenclature_code, turn,  comments,  period)
values('79c9f71e-926f-11ee-b9d1-0242ac120002', 0, 'Начальный остаток','2023-10-01 00:00');

insert into history(nomenclature_code, turn,  comments,  period)
values('79c9f71e-926f-11ee-b9d1-0242ac120002', -5, 'Списание','2023-11-02 15:00');
```
 


#### Задания
1. Дописать модульный тест на `Python`: history_test. 
	- Добавить генерацию данных по несколько исторических записей в рамках каждого кода номенклатуры.
	- Добавить обязательные проверки в метод `test_get_nomenclature_history` на :
		- Наличие отрицательных сумм
		- Отсутствие нулевых сумм 
2. Написать [Фабричный метод](https://github.com/VolovikovAlexander/Patterns/tree/main/Step4) для конвертации массива моделей `nomenclature_hostory` в массив моделей `nomenclature_balance`
3. Написать модульные тесты для проверки работы Фабричного метода
4. Открыть и изучить базу данных `storage` (SQLite)

##### Дополнительно
	- Сформировать 10 000 записей в методе `test_get_nomenclature_history` и  в базе данных: таблица `history`	
	- Сделать сравнительный анализ производительности (с замером времени) на преобразование в модель `nomenclature_balance`
	  по обеим вариантам: `Python`, `SQLite`



