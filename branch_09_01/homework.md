# Практика работы с настройками
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Результат](#результат)


## Задание
Данное задание делится на несколько частей:
1. **Использование base_url для инициализации страниц и рефакторинг хардкода ссылок во всем проекте.**
2. **Рефакторинг хардкода данных тестового пользователя.**
3. **Рефакторинг хардкода путей к тестовым файлам.**

### Часть 1: Использование base_url для инициализации страниц и рефакторинг хардкода ссылок во всем проекте
#### Зачем это нужно?
Использование base_url даёт нам глобальный entry point для построения всех ссылок в проекте. Это позволяет избежать необходимости передавать настройки и URL приложения везде. Достаточно лишь прописать часть пути, например, "/#/auth/registration".

Применение enum AppRoute обеспечивает защиту от ошибок при написании маршрутов. В случае изменения URL на странице регистрации, с /#/auth/registration на /#/registration, если это изменение используется в 200 автотестах, не потребуется редактировать каждый тест вручную. Достаточно будет обновить значение в enum AppRoute, и все автотесты автоматически адаптируются к новому пути.

#### Шаги выполнения:
1. Добавление метода *get_base_url* в модель Settings.
    В файле config.py добавьте следующий метод:
    ```python
    class Settings(BaseSettings):
    # Остальной код без изменений

    def get_base_url(self) -> str:
        return f"{self.app_url}/"
    
    # Остальной код без изменений
    ```
    Это необходимо для корректной передачи base_url в Playwright.
2. Добавление *base_url* при инициализации контекста в функции *initialize_playwright_page*.
    В файле tools/playwright/pages.py обновите функцию *initialize_playwright_page*:
    ```python
    context = browser.new_context(
        base_url=settings.get_base_url(),  # Необходимо добавить settings.get_base_url()
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
        )
    ```
    Теперь все ссылки будут начинаться с *https://nikita-filonov.github.io/qa-automation-engineer-ui-course/*. 
    Это означает, что при использовании метода *visit*, можно будет указывать только путь:
    - До использования *base_url*
        ```python
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        ```
    - После использования base_url:
        ```python
        registration_page.visit("./#/auth/registration")
        ```
3. Добавление *base_url* в фикстуру *initialize_browser_state*
    В фикстуре *initialize_browser_state* также нужно добавить *base_url*
    ```python
    @pytest.fixture(scope="session")
    def initialize_browser_state(playwright: Playwright):
        # Остальной код без изменений
        context = browser.new_context(base_url=settings.get_base_url())
        # Остальной код без изменений
    ```
4. Создание файла *tools/routes.py*
    Создайте файл *tools/routes.py*
5. Добавление *enum AppRoute*
    В файле tools/routes.py добавьте enum AppRoute
    ```python
    from enum import Enum

    class AppRoute(str, Enum):
        LOGIN = "./#/auth/login"
        REGISTRATION = "./#/auth/registration"
        DASHBOARD = "./#/dashboard"
        # Добавьте все остальные маршруты
    ```
6. Применение *enum AppRoute* во всем проекте.
    - До использования *AppRoute*
    ```python
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    ```
    - После использования *AppRoute*
    ```python
    registration_page.visit(AppRoute.REGISTRATION)
    ```
#### Критерии выполнения:
- В проекте больше нет захардкоженных ссылок в виде:
```python
registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
```
- Все ссылки используются через *base_url* и *enum AppRoute*

[вверх](#практика-работы-с-настройками)


### Часть 2: Рефакторинг хардкода данных тестового пользователя

#### Зачем это нужно?
Данные тестового пользователя могут меняться. Например, может потребоваться регулярная очистка базы данных, перенастройка тестового пользователя, использование разных пользователей на разных окружениях (dev, stable, staging). В таких случаях гибкое хранение данных тестового пользователя в одном месте позволяет легко адаптировать автотесты без необходимости вносить изменения в код автотестов.

#### Шаги выполнения
1. В рамках этой части задания вам необходимо рефакторить код и заменить хардкоженные данные пользователя на использование настроек:
    - До рефакторинга:
    ```python
    registration_page.registration_form.fill(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    ```
    - После рефакторинга:
    ```python
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    ```
2. В некоторых местах могут быть захардкожены данные пользователя, например:
    ```python
    dashboard_page_with_state.navbar.check_visible("username")
    ```
    Это также нужно исправить, используя настройки:
    ```python
    dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
    ```
#### Исключение:
Параметризация остается неизменной:
```python
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", " "),
        (" ", "password")
    ]
)
```

#### Критерии выполнения:
- В проекте больше нет захардкоженных данных тестового пользователя (кроме параметризации). Все данные пользователя берутся из настроек.

[вверх](#практика-работы-с-настройками)


### Часть 3: Рефакторинг хардкода путей к тестовым файлам

#### Зачем это нужно?
Хардкод путей к тестовым файлам может вызвать проблемы при изменении структуры директорий, переименовании файлов или папок. Использование настроек для хранения путей делает проект более гибким и устойчивым к изменениям.

#### Шаги выполнения:
1. Замените хардкоды путей к тестовым файлам:
    - До рефакторинга:
    ```python
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    ```
    - После рефакторинга:
    ```python
    create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
    ```
2. Настройки для путей к файлам должны быть прописаны в *.env* файле и использоваться через объект *settings*.

#### Критерии выполнения:
В проекте больше нет хардкода путей к тестовым файлам. Все пути к файлам берутся из настроек.

[вверх](#практика-работы-с-настройками)


### Тестирование

После завершения рефакторинга запустите все автотесты, чтобы убедиться, что они работают корректно и успешно проходят:
```python
python -m pytest -m "regression"
```

[вверх](#практика-работы-с-настройками)


### Критерии успешного выполнения

1. Base URL и роуты
    - Реализован метод *Settings.get_base_url()* и он используется при создании контекста
        - в *tools/playwright/pages.py* (*browser.new_context(base_url=...)*);
        - в фикстуре *initialize_browser_state (base_url=...)*.
    - Создан *tools/routes.py* с *AppRoute* (как минимум: *LOGIN*, *REGISTRATION*, *DASHBOARD*, *COURSES*, *COURSES_CREATE*).
    - Все значения *AppRoute* начинаются с *./* (например, *./#/auth/login*)
    - Во всём проекте переходы выполняются через *visit(AppRoute.XXX)* вместо абсолютных URL
    - В проекте не осталось захардкоженных полных ссылок.
2. Данные тестового пользователя
    - Везде, где это логично, хардкод заменён на настройки:
        - формы/проверки используют *settings.test_user.email/username/password*;
        - примеры: *registration_page.registration_form.fill(...)*, *navbar.check_visible(settings.test_user.username)*
        - Негативная параметризация (в *@pytest.mark.parametrize*) оставлена как есть — хардкод допустим
3. Пути к тестовым файлам
    - Хардкод путей к файлам заменён на настройки, например:
        - *settings.test_data.image_png_file* вместо *'./testdata/files/image.png'*.
4. Запуск и качество
    - Все тесты успешно проходят командой: *python -m pytest -m "regression"*.
    - Код чистый и аккуратный, без дублирования, соответствует PEP8.

[вверх](#практика-работы-с-настройками)


## Результат
```sh
vscode@0d3ee56b7865:~/workspace$ pytest -m 'regression'
====================== test session starts =====================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 55 items / 45 deselected / 10 selected
tests/authentication/test_authorization.py::TestAuthorization::test_wrong_email_or_password_authorization[user.name@gmail.com-password] PASSED
tests/authentication/test_authorization.py::TestAuthorization::test_wrong_email_or_password_authorization[user.name@gmail.com-  ] PASSED
tests/authentication/test_authorization.py::TestAuthorization::test_wrong_email_or_password_authorization[  -password] PASSED
tests/authentication/test_authorization.py::TestAuthorization::test_successful_authorization PASSED
tests/authentication/test_authorization.py::TestAuthorization::test_navigate_from_authorization_to_registration PASSED
tests/authentication/test_registration.py::TestRegistration::test_successful_registration PASSED
tests/courses/test_courses.py::TestCourses::test_empty_courses_list PASSED
tests/courses/test_courses.py::TestCourses::test_create_course PASSED
tests/courses/test_courses.py::TestCourses::test_edit_course PASSED
tests/dashboard/test_dashboard.py::TestDashboard::test_dashboard_displaying PASSED

====================== 10 passed, 45 deselected in 89.69s (0:01:29) ============
```

[вверх](#практика-работы-с-настройками)