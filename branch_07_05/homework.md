# Практика работы с Page Factory
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Результат](#результат)

## Задание
В этом задании вам предстоит самостоятельно применить компоненты Page Factory для следующих страниц и компонентов:
1. *LoginFormComponent*
2. *RegistrationPage*
3. *RegistrationFormComponent*
4. *NavbarComponent*
5. *SidebarComponent*
6. *SidebarListItemComponent*
7. *EmptyViewComponent*
8. *ImageUploadWidgetComponent*
9. *DashboardToolbarViewComponent*

Для всех перечисленных выше компонентов вам необходимо:
1. Применить подход Page Factory для организации элементов страниц и компонентов.
2. Адаптировать методы взаимодействия с элементами, используя структуру Page Factory.
3. Реализовать использование таких элементов, как *Input*, *FileInput*, *Button*, *Icon*, *Image*, *Text* и других, которые мы рассматривали в ходе урока. Важно учесть, что каждый элемент должен принимать аргумент *name*, представляющий собой человекочитаемое описание элемента. В результате, каждый элемент должен быть преобразован следующим образом:
  - **До использования Page Factory**:
    ```python
    self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
    ```
  - **После использования Page Factory**:
    ```python
    self.email_input = Input(page, 'login-form-email-input', 'Email')
    ```
4. Убедиться, что автотесты успешно работают с обновленными страницами и компонентами после внедрения Page Factory.

После внесения изменений, выполните команду для запуска автотестов:
```sh
python -m pytest -m "regression" -s -v
```

**Критерии успешного выполнения**:
- В существующих компонентах и страницах **все обращения к локаторам** (*page.locator*, *page.get_by_test_id*) заменены на фабричные элементы (*Input*, *Button*, *Text*, *Icon*, *Image*, *FileInput*, *Link*).
Например:
  - До: *self.email_input = page.get_by_test_id('login-form-email-input').locator('input')*
  - После: *self.email_input = Input(page, 'login-form-email-input', 'Email')*
- Каждый элемент инициализируется с человекочитаемым аргументом name (например: *'Email'*, *'Password'*, *'Upload image'*).
- Методы взаимодействия (*fill*, *click*, *set_input_files*) и проверки (*check_visible*, *check_have_text*, *check_have_value*) выполняются через элементы, а не напрямую через *expect* или *page.locator*.
- Логика компонентов и страниц сохранена:
  - *LoginFormComponent* и *RegistrationFormComponent* используют *Input*.
  - *RegistrationPage* работает с *Link* и *Button*.
  - *NavbarComponent* проверяет заголовки через *Text*.
  - *SidebarComponent* и *SidebarListItemComponent* используют *SidebarListItemComponent* с элементами *Icon*, *Text*, *Button*.
  - *EmptyViewComponent* проверяет *Icon*, *Title*, *Description* через элементы.
  - *ImageUploadWidgetComponent* комбинирует *EmptyViewComponent*, *FileInput*, *Image*, *Button*, *Text*.
  - *DashboardToolbarViewComponent* проверяет заголовок через *Text*.
- В коде компонентов и страниц нет прямых вызовов:
  - *page.get_by_test_id(...)*
  - *page.locator(...)*
  - *expect(...)*
  - Всё инкапсулировано в элементах.
- После рефакторинга автотесты запускаются командой:
```sh
python -m pytest -m "regression" -s -v
```
- Код чистый, структурированный, соответствует принципам Page Object + Page Factory, без дублирования и «сырых» локаторов.
- Соблюдены принципы PEP8 (отступы, названия переменных, длина строк).

[вверх](#практика-работы-с-page-factory)


## Результат
```sh
vscode@d9054007f115:~/workspace$ source ./run_flake8.sh 
vscode@d9054007f115:~/workspace$ pytest -s -v -m 'regression'
=============================== test session starts ============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 45 deselected / 7 selected

tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-password] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-  ] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[  -password] PASSED
tests/test_courses.py::test_empty_courses_list PASSED
tests/test_courses.py::test_create_course PASSED
tests/test_dashboard.py::test_dashboard_displaying PASSED
tests/test_registration.py::test_successful_registration PASSED

=============================== 7 passed, 45 deselected in 27.88s ==============
```

[вверх](#практика-работы-с-page-factory)