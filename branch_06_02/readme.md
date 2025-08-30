# 6.2 Интеграция Pytest и Playwright
[назад](../readme.md)

## Преобразуем скрипты в автотесты

Файл ./src/tests/test_successfull_registration.py - автотест регистрации нового пользователя  
Файл ./src/tests/test_authorization.py - автотест авторизации в приложении  
Файл ./src/tests/test_courses.py - автотест проверки того, что у свежезарегистрированного пользователя нет доступных курсов  


### Заметки по работе
Использую заранее собранный докер-образ на базе python3.12-bookworm с установленными пакетами pytest, playwright+browsers, allure, flake8, isort.    
Также внедрен openssh server для удаленной разработки с VS Code.
Исходники в папке /docker репозитория

Запуск образа из каталога с заданием проекта
```sh
source ./run_pw_v2.sh
```
после запуска образа подкаталог ./src будет примаплен в подкаталог ./workspace домашней директории пользователя vscode
```
./src -> /home/vscode/workspace/
```
Можно подключиться с VS Code или через PUTTY  
Действия внутри поднятого контейнера после логина

прогнать фикс импортов isort (опционально)
```sh
isort ./workspace
```
прогнать линтинг Flake8 (опционально)
```sh
flake8 ./workspace
```
и запустить тесты
```sh
pytest -s -v
```


### Практика написания автотестов
В данном задании необходимо написать автотест на основе скрипта в файле playwright_courses.py:
- Создать файл tests/test_courses.py
- Внутри файла tests/test_courses.py создать тестовую функцию и назвать ее test_empty_courses_list
- В тело функции необходимо поместить скрипт из файла playwright_courses.py (из branch_05_06)  

#### Критерии выполнения задания
- **Структура файлов**
    - Создан файл **tests/test_courses.py**.
    - В файле объявлена тест-функция **test_empty_courses_list**.
- **Логика теста (по сути сценарий из playwright_courses.py)**
    - Тест выполняет регистрацию пользователя и сохраняет **состояние браузера**.
    - Запускает **новую** сессию/контекст с подключением сохранённого состояния.
    - Открывает страницу **#/courses** без повторной авторизации.
    - Проверяет элементы на странице **Courses**:
        - Заголовок **"Courses"** – наличие и корректный текст.
        - Иконка пустого списка – наличие/видимость.
        - Заголовок пустого блока **"There is no results"** – наличие и текст.
        - Описание пустого блока **"Results from the load test pipeline will be displayed here"** – наличие и текст.
- **Запуск и результат**
    - Тест запускается командой *python -m pytest -s -v* и **успешно проходит**.
    - Исполнение завершается **без ошибок**.
- **Качество реализации**
    - Используются **стабильные селекторы** (например, по data-test-id).
    - Нет ненужных *sleep*; используются ожидания/автоожидания Playwright.
    - Код **аккуратный**, соответствует **PEP8** (отступы, именование, длина строк).

Результат:
```
vscode@8520b2f578e4:~$ flake8 ./workspace
vscode@8520b2f578e4:~$ pytest -s -v
============================================= test session starts ==============================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 3 items

workspace/tests/test_authorization.py::test_wrong_email_or_password_authorization PASSED
workspace/tests/test_courses.py::test_empty_courses_list PASSED
workspace/tests/test_successful_registration.py::test_successful_registration PASSED

============================================== 3 passed in 19.42s ==============================================
```
