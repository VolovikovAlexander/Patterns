# Занятие № 14
**Шаблон CQRS**

Цель:
- Новый архитектурный шаблон `CQRS`
- Закрепить опыт работы с `Docker`
- Работа с СУБД Postgres
 
## Выполнить
* Доработка системы сборки. Сборка нового образа на основе Web сервера `NGinx`
* Совместное проектирование базы данных для хранения данных. 
* Разработка класса `database_service`. Примеры взаимодействия с базой данных.
* Модульные тесты.

## Задание
1. Необходимо доработать `docker-compose`, `Dockerfile` и настройки `NGinx`. 
   Необходимо разделить на два хоста систему. 
  	- Первый хост работает со всеми `GET` запросами
  	- Второй с остальными запросами.
2. Необходимо доработать сервис `database_service` для чтения и записи данных в базу данных. 
  Добавить два метода (или доработать существующие)
   - `POST` \api\save
   - `POST` \api\load 
3. Добавить настройки (`settings.json`) для хранения строки подключения к базу данных и режима работы с хранилищем данных.
   - Записывать \ считывать из базы данных
   - Записывать \ считывать из файла
   - Настройки для подключения к базе данных сделать с использованием `Environment` (.env файл)
4. Используя файлы с запросами к сервисам (8001, 8002 порты, bat / sh файлы / подготовленные в прошлом задании) 
  запустить запрос на изменение любой сущности (например: наименование в номенклатуре), далее, 
  запустить сохранение данные (POST api\save) на одном из сервисов, а на другом сервисе сформировать `POST` api\load и потом `GET` запрос. 
5. Результаты выполнения **пункта 4** показать в виде изображение + логи. Вложить в PullRequest результаты.

