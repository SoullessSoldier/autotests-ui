# 6.7 Параметризация в pytest
[назад](../readme.md)

Содержание:
- [Преимущества параметризации](#преимущества-параметризации)
- [Основные методы параметризации](#основные-методы-параметризации)
- [Параметризация тестов с помощью @pytest.mark.parametrize](#параметризация-тестов-с-помощью-pytestmarkparametrize)
- [Параметризация фикстур](#параметризация-фикстур)
- [Полезные приемы параметризации](#полезные-приемы-параметризации)
- [Практика](#практика)
- [Практика работы с pytest параметризацией](#практика-работы-с-pytest-параметризацией)


Файлы ./tests/*.py - файлы практики

## Преимущества параметризации:
- Экономия времени: один тест покрывает сразу несколько вариантов.
- Поддерживаемость: уменьшается количество дублирующего кода.
- Гибкость: легко добавлять новые тестовые данные.

## Основные методы параметризации
- Параметризация тестов с помощью @pytest.mark.parametrize
- Параметризация фикстур

## Параметризация тестов с помощью @pytest.mark.parametrize
```python
import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("admin", "admin123")
])
def test_login(username, password):
    assert login(username, password) == "Success"
```
Параметризация с pytest.param:

Иногда нужно передать не только значения, но и дополнительную информацию, например, отметить, что тест должен быть пропущен или ожидать конкретного исключения. 
```python
@pytest.mark.parametrize("value", [
    pytest.param(1),
    pytest.param(2),
    pytest.param(-1, marks=pytest.mark.skip(reason="Negative value")),
])
def test_increment(value):
    assert increment(value) > 0
```
                  
В этом примере третий тест будет пропущен, так как он помечен pytest.mark.skip

[вверх](#67-параметризация-в-pytest)


## Параметризация фикстур
Параметризовать можно не только тестовые функции, но и фикстуры. Это полезно, когда нужно передать разные параметры в фикстуру, а затем использовать их в разных тестах.
```python
import pytest

@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request):
    return request.param

def test_browser(browser):
    assert browser in ["chrome", "firefox", "safari"]
```

[вверх](#67-параметризация-в-pytest)


## Полезные приемы параметризации
### Параметризация с помощью словарей
Иногда удобнее передавать значения в виде словарей, особенно если параметры могут изменяться:
```python
@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login(data):
    assert login(data["username"], data["password"]) == "Success"
```
                  
### Комбинированная параметризация
Можно комбинировать несколько параметров, чтобы создавать тесты с перекрестными комбинациями значений:
```python
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@pytest.mark.parametrize("os", ["windows", "mac"])
def test_cross_platform(browser, os):
    assert run_test(browser, os) == "Success"
```
                  
В этом примере тесты будут выполнены для каждой комбинации browser и os (всего 4 комбинации).
                  
Здесь фикстура browser будет передавать различные значения браузеров, и тест test_browser выполнится три раза — по одному на каждый браузер.

[вверх](#67-параметризация-в-pytest)

## Практика
1) базовый случай
```python
@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
def test_numbers(number: int):
    assert number > 
```
2) несколько параметров
```python
@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected
```
3) перемножение параметров
```python
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0
```
4) параметризация фикстур
```python
from _pytest.fixtures import SubRequest

@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"

# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")
```
5) параметризация классов
```python
# Для тестовых классов параметризациф указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")
```
6) идентификаторы
```python
@pytest.mark.parametrize(
    "phone_number",
    ["+70000000011", "+70000000022", "+70000000033"],
    ids=[
        "User with money on bank account",
        "User without money on bank account",
        "User with operations on bank account"
    ]
)
def test_identifiers(phone_number: str):
    pass
```
7) динамические идентификаторы
```python
# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number", 
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass

```

[вверх](#67-параметризация-в-pytest)


## Практика работы с pytest параметризацией
В рамках данного задания необходимо параметризировать уже существующий автотест *test_wrong_email_or_password_authorization*.
В качестве параметров используйте значения для *email* и *password*. Тест должен запускаться трижды с различными комбинациями параметров
| Тест-кейс | Email | Password |
|-----------|-------|----------|
|Проверяем, что пользователь не может войти в систему с невалидными email и password | "user.name@gmail.com" | "password" |
|Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password | "user.name@gmail.com" | "  " (два пробела) |
|Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password | "  " (два пробела) | "password" |
Каждый тест должен использовать параметризированные значения *email* и *password*, передавая их в качестве аргументов функции теста.

Автотест должен запускаться данной командой:
```sh
python -m pytest -k "test_wrong_email_or_password_authorization" -s -v
```
                  
Тест должен успешно проходить, все должно быть запущено 3 автотеста

### Пример параметризованного автотеста
Аргументы параметризованного автотеста должны выглядеть следующим образом:
```python
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
```

### Критерии выполнения задания
- Структура файлов
  - Автотест *test_wrong_email_or_password_authorization* находится в файле *tests/test_authorization.py*.
- Параметризация
  - Тест помечен декоратором *@pytest.mark.parametrize*.
  - Аргументы функции теста: *chromium_page: Page, email: str, password: str*.
  - Указаны три набора параметров:
    1. *("user.name@gmail.com", "password")*
    2. *("user.name@gmail.com", "  ")* (два пробела в password)
    3. *("  ", "password")* (два пробела в email)
  - В каждом запуске теста значения параметров передаются в поля формы.
- Маркировка теста
  - У теста есть маркировки: regression и authorization.
- Логика теста
  - Открывается страница логина.
  - Заполняются поля **Email** и **Password** параметризованными значениями.
  - Нажимается кнопка **Login**.
  - Проверяется наличие и текст алерта:
    - Элемент виден.
    - Текст равен "**Wrong email or password**".
- Запуск и результат
  - Тест запускается командой:
  ```python
  python -m pytest -k "test_wrong_email_or_password_authorization" -s -v
  ```
  - Тест выполняется трижды (по числу параметров).
  - Все три прогона завершаются успешно.
- Качество реализации
  - Используются **стабильные селекторы** (*data-test-id*).
  - Нет дублирования кода (логика повторного ввода сведена к параметрам).
  - Код соответствует **PEP8** (отступы, длина строк, форматирование).

### Результат:
```sh
vscode@a5c94413a190:~/workspace$ flake8 ./tests/      
vscode@a5c94413a190:~/workspace$ pytest -s -v -k 'test_wrong_email_or_password_authorization'
=============================== test session starts ============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: playwright-0.7.0, base-url-2.1.0, allure-pytest-2.15.0
collected 34 items / 31 deselected / 3 selected                                                                                                                                        

tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-password] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-  ] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[  -password] PASSED

=============================== 3 passed, 31 deselected in 18.82s ==============
```

[вверх](#67-параметризация-в-pytest)


Ссылки:
- [Официальная документация pytest по параметризации](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)

[вверх](#67-параметризация-в-pytest)

