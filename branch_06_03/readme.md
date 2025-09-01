# 6.3 Маркировки Pytest
[назад](../readme.md)

Содержание:
- [Практика работы с pytest маркировками](#практика-работы-с-pytest-маркировками)
- [Рабочие материалы](#рабочие-материалы)


## Практика работы с pytest маркировками

В данном задании вам необходимо добавить маркировки к автотесту test_empty_courses_list, который находится в файле *tests/test_courses.py*:
- Добавить pytest маркировки **courses**, **regression** к автотесту *test_empty_courses_list*
- Зарегистрировать новые маркировки в файле *pytest.ini*

Автотест должен запускаться командой:
```sh
python -m pytest -m courses
```
или 
```sh
python -m pytest -m regression
```

### Критерии выполнения задания
- **Структура файлов**
  - В проекте уже существует файл *tests/test_courses.py* с тестом *test_empty_courses_list*.
  - Создан или дополнен файл pytest.ini в корне проекта.
- **Маркировка теста**
  - К тестовой функции *test_empty_courses_list* добавлены маркировки:
    - *@pytest.mark.courses*
    - *@pytest.mark.regression*
- **Регистрация маркировок**
  - В файле *pytest.ini* зарегистрированы новые маркировки:
    - *courses* – для тестов, связанных с курсами.
    - *regression* – для регрессионных тестов.
- **Запуск тестов**
  - Тест успешно запускается и проходит при вызове:
    - *python -m pytest -m courses*
    - *python -m pytest -m regression*
- *Качество реализации*
  - Конфигурация в *pytest.ini* оформлена корректно, без ошибок синтаксиса.
  - Код аккуратный, соответствует **PEP8**.


### Результат:
```sh
vscode@c4333d0c0844:~/workspace$ flake8 ./tests/
vscode@c4333d0c0844:~/workspace$ pytest -m courses ./tests/
===================== test session starts ======================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item
tests/test_courses.py .     [100%]
===================== 1 passed in 4.51s ========================================
vscode@c4333d0c0844:~/workspace$ pytest -m regression ./tests/
===================== test session starts ======================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item         
tests/test_courses.py .     [100%]
===================== 1 passed in 4.44s ========================================
```
[вверх](#63-маркировки-pytest)


## Рабочие материалы

Для запуска тестов с определенной маркировкой используйте опцию -m с именем маркировки:
```sh
pytest -m smoke
```

Если в проекте есть *pytest.ini*, то простой запуск pytest будет вызывать ошибки,  
и надо запускать его с опцией **--disable-warnings**
```sh
vscode@c4333d0c0844:~/workspace$ pytest -v -m smoke_class --disable-warnings
===================== test session starts ======================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 4 items / 2 deselected / 2 selected
test_mark_1.py::TestSuite::test_case1 PASSED
test_mark_1.py::TestSuite::test_case2 PASSED
```

Маркировка класса и отдельных тестов внутри класса
```sh
pytest -v -m "regression and not slow" --disable-warnings
```
Составные маркировки
```sh
pytest -v -m "smoke or critical" --disable-warnings
```
```sh
pytest -v -m "ui and regression" --disable-warnings
```
```sh
vscode@c4333d0c0844:~/workspace$ pytest test_successfull_registration.py -m registration -v --disable-warnings
======================== test session starts ===================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item
test_successfull_registration.py::test_successful_registration   PASSED   [100%]
======================== 1 passed, 2 warnings in 10.87s ========================
```

Если создать pytest.ini в каталоге с фалами тестов, то можно запускать pytest без опции --disable-warnings
```sh
pytest test_successfull_registration.py -m registration -v
```
```sh
pytest -s -v -m authorization test_wrong_email_or_password_authorization.py 
======================== test session starts ===================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item 
test_wrong_email_or_password_authorization.py::test_wrong_email_or_password_authorization PASSED

======================== 1 passed in 2.13s =====================================
```
Ссылки:

[Официальная документация Pytest по регистрации маркировок](https://docs.pytest.org/en/stable/example/markers.html#registering-markers)

[вверх](#63-маркировки-pytest)