# Список задач для сдачи зачета

1. Реализовать шаблон `одиночка` для хранения и управления свойствами модели: `организация`. Свойства модели: код, наименование, адрес, почтовый индекс.
Обязательно реализовать автотесты для проверки работы кода.

2. Реализовать создание списка моделей произвольным образом. 
модель: `Пользователь`. Свойства модель: код, логин, пароль, наименование, почтовый адрес.
Обязательно реализовать автотесты для проверки работы кода.

3. Реализовать шаблон `фабричный метод`. Необходимо использую шаблон создавать различные модели: склад, организация, пользователь.
Обязательно реализовать автотесты для проверки работы кода.

4. Реализовать шаблон `фабрика`. Реализовать два класса которые будут сохранять данные в текстовый файл в разных форматах. Добавить
фабрику в параметры которой будет передаваться модель и формат. В зависимости от формата фабрика должна создавать нужный класс, а далее
реализовать сохранение данных модели в файл в нужном формате. модель: пользователь. Свойства модели: код, наменование, пароль, почтовый адрес
Обязательно реализовать автотесты для проверки работы кода.

5. Реализовать шаблон `прототип`. Добавить список моделей пользователь. Свойства модели: код, наменование, пароль, почтовый адрес
Добавить в шаблон поиск по: наименованию, почтовому адресу.
Обязательно реализовать автотесты для проверки работы кода.

6. Реализовать набор моделей Пользователь, организация, склад. Во всех моделях нужно реализовать общий метод: `to_str`
с использованием механизма наследования. Данный метод должен формировать текстовое представление модели: код + наименование
Во всех моделях два поля общие (одинаковые): код, наименование.
Обязательно реализовать автотесты для проверким работы кода



