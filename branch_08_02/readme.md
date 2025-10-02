# 8.2 Интеграция Allure в автотесты
[назад](../readme.md)

Содержание:
- [Allure аннотации: @allure.title](#allure-аннотации-alluretitle)
- [Allure аннотации: @allure.tag](#allure-аннотации-alluretag)
- [Allure аннотации: @allure.epic, @allure.feature, @allure.story](#allure-аннотации-allureepic-allurefeature-allurestory)
- [Allure аннотации: @allure.severity](#allure-аннотации-allureseverity)
- [Практическая работа с Allure аннотациями (домашняя работа)](#практическая-работа-с-allure-аннотациями-домашняя-работа)


## Allure аннотации: @allure.title

### Изменение заголовка автотеста в Allure
По умолчанию, Allure использует название тестовой функции в качестве заголовка для автотеста в отчёте.  
Для того чтобы сделать заголовок автотеста более понятным, можно использовать аннотацию *@allure.title*:
```python
import allure

@allure.title("User login with wrong email or password")  # Добавляем человекочитаемый заголовок
def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
    pass
```

### Динамическое изменение заголовка
Если вам нужно изменить заголовок в процессе выполнения теста (например, в зависимости от параметров),  
можно использовать метод *allure.dynamic.title*
```python
@allure.title("User login with wrong email or password")  # Заголовок через декоратор — рекомендуется
def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
    allure.dynamic.title(f"Attempt to login with email: {email}")  # Заголовок через allure.dynamic.title

```

### Как правильно писать заголовки для автотестов
- **Краткость и ясность**. Заголовок должен быть коротким, но при этом чётко описывать суть автотеста.
- **Человекочитаемость**. Заголовок должен быть понятен не только разработчику, но и любому члену команды, например, ручному тестировщику или менеджеру.
- **Фокус на суть теста**. Заголовок должен отвечать на вопрос: "Что проверяет данный автотест?".

### Добавление @allure.title ко всем автотестам
Добавляем аннотацию @allure.title заголовки ко всем автотестам:
- /tests/authentication/test_authorization.py
- /tests/authentication/test_registration.py
- /tests/courses/test_courses.py
- /tests/dashboard/test_dashboard.py

[вверх](#82-интеграция-allure-в-автотесты)


## Allure аннотации: @allure.tag

Теги Allure похожи на маркировки pytest, но используются исключительно для фильтрации отчётов, предоставляя метаинформацию о тесте. В то время как pytest-маркировки применяются для запуска тестов, теги Allure помогают структурировать отчёт.

По умолчанию автотесты в Allure отчете содержат теги, которые берутся из pytest маркировок:

### Синтаксис тегов

Важно соблюдать единый формат написания тегов, рекомендуется использовать следующий стиль:
- Теги должны быть в формате *UPPER_SNAKE_CASE*.
- Теги должны быть константами или перечислениями (enum).

Как было отмечено выше, использование enum уменьшает вероятность ошибок при работе с тегами.  
Добавим файл *tags.py* в папку *tools/allure*

Добавление @allure.tag ко всем автотестам:
```python
import allure
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag # Импортируем enum с тегами


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION) # Добавили теги
class TestRegistration:
    # Остальной код без изменений
```

[вверх](#82-интеграция-allure-в-автотесты)


## Allure аннотации: @allure.epic, @allure.feature, @allure.story

Разберём три ключевые аннотации в Allure: *@allure.epic*, *@allure.feature* и *@allure.story*. Эти аннотации помогают структурировать отчёты, связывая автотесты с функциональными блоками системы, которые они проверяют.
1. *@allure.epic*
  **Epic** — это крупная часть продукта, объединяющая функциональные блоки, которые решают крупные задачи системы. Это уровень самого высокого абстрактного представления, например, проект или модуль в системе.

2. *@allure.feature*
  **Feature** — это функциональная возможность продукта, более конкретная, чем epic, но всё ещё широкого охвата. Feature описывает отдельные аспекты системы, такие как конкретные модули или крупные функции.

3. *@allure.story*
  **Story** — это конкретный пользовательский сценарий или задача, описывающая конкретные действия, которые может совершать пользователь или система. Story является самой детализированной аннотацией, используемой для описания автотестов.

### Хранение epic, feature и story в enum
Для удобства и уменьшения риска ошибок при использовании аннотаций epic, feature и story, лучше всего хранить их значения в enum-ах.
```text
.
└── tools/
    ├── __init__.py
    └── allure/
        ├── __init__.py
        ├── tags.py
        ├── epics.py
        ├── stories.py
        └── features.py
```

Пример использования в тестовом классе *TestAuthorization*:
```text
import allure
import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.AUTHORIZATION) # Добавили story
class TestAuthorization:
    # Остальной код без изменений

```

На вкладке **Behaviors** в Allure-отчёте вы увидите древовидную структуру, в которой тесты будут организованы по epic, feature и story. Это позволит легко фильтровать и анализировать тесты на уровне функциональных блоков и сценариев.

### Добавление @allure.epic, @allure.feature, @allure.story ко всем автотестам
Теперь добавим аннотацию @allure.epic, @allure.feature, @allure.story заголовки ко всем остальным автотестам.

[вверх](#82-интеграция-allure-в-автотесты)


## Allure аннотации: @allure.severity

### Что такое уровень важности (severity) автотеста?
Уровень важности или критичности (severity) указывает на значимость функционала, который проверяется автотестом. Этот параметр позволяет оценить, насколько критично работоспособность данного функционала для всего приложения. Например, такие процессы, как авторизация и регистрация, почти всегда считаются критичными, поскольку без них пользоваться приложением нельзя. В то же время такие функции, как отображение даты рождения в профиле пользователя, являются менее важными.

### Какие уровни важности бывают?
Обычно выделяют пять уровней критичности:
- **blocker** — Самый важный функционал. Если он не работает, то пользоваться приложением невозможно.
- **critical** — Очень важный функционал. Если он сломан, приложение будет бесполезным с точки зрения бизнес-логики, хотя некоторые функции могут работать.
- **normal** — Важный функционал. Если он не работает, это создаст неудобства для пользователя, но есть обходные пути.
- **minor** — Некритичный функционал. Даже если он не работает, приложение остается полностью функциональным.
- **trivial** — Совершенно незначительный функционал. Например, визуальные несоответствия, такие как кнопка, которая больше на 1 пиксель или слегка неправильный цвет.

В Allure уже встроен enum с уровнями важности:
```python
from enum import Enum


class Severity(str, Enum):
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'
```
### Пример использования аннотации @allure.severity
Аннотацию @allure.severity можно добавлять как на уровне тестового класса, так и на уровне конкретного теста.  
Давайте рассмотрим пример использования на основе класса *TestAuthorization*
```python
import allure
import pytest
from allure_commons.types import Severity # Импортируем enum Severity из Allure

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL) # Добавили severity
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        # Остальной код без изменений

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER) # Добавили severity
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        # Остальной код без изменений

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL) # Добавили severity
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        # Остальной код без изменений

```

Теперь в деталях каждого теста в отчёте Allure будет отображаться уровень его важности.


[вверх](#82-интеграция-allure-в-автотесты)


## Практическая работа с Allure аннотациями (домашняя работа)
[ссылка на описание домашней работы](./homework.md)

[вверх](#82-интеграция-allure-в-автотесты)