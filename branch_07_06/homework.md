# Практикуемся в применении Page Factory
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Критерии успешного выполнения](#критерии-успешного-выполнения)
- [Результат](#результат)

## Задание
В этом задании вам предстоит самостоятельно применить компоненты Page Factory для следующих страниц и компонентов:
1. *CoursesListToolbarViewComponent*
2. *CreateCourseExercisesToolbarViewComponent*
3. *CreateCourseFormComponent*
4. *CreateCourseToolbarViewComponent*

Для всех перечисленных выше компонентов вам необходимо:
1. Применить подход Page Factory для организации элементов страниц и компонентов.
2. Адаптировать методы взаимодействия с элементами, используя структуру Page Factory.
3. Реализовать использование таких элементов, как *Input*, *Textarea*, *Button*, *Icon*, *Image*, *Text* и других. Важно учесть, что каждый элемент должен принимать аргумент name, представляющий собой человекочитаемое описание элемента. В результате, каждый элемент должен быть преобразован следующим образом:

    **До использования Page Factory:**  
        ```python
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        ```

    **После использования Page Factory:**  
        ```python
        self.email_input = Input(page, 'login-form-email-input', 'Email')
        ```
4. Убедиться, что автотесты успешно работают с обновленными страницами и компонентами после внедрения Page Factory.

После внесения изменений, выполните команду для запуска автотестов:
```sh
python -m pytest -m "regression" -s -v
```

[вверх](#практикуемся-в-применении-page-factory)


## Критерии успешного выполнения
- В существующих компонентах все обращения к локаторам (*page.locator*, *page.get_by_test_id*) заменены на 
фабричные элементы (*Input, *Textarea*, *Button*, *Text* и другие).  
Например:  
    - **До:** *self.email_input = page.get_by_test_id('login-form-email-input').locator('input')*  
    - **После:** *self.email_input = Input(page, 'login-form-email-input', 'Email')*
- Каждый элемент инициализируется с человекочитаемым аргументом name (например: *'Title'*, *'Description'*, *'Create course'*).
- Методы взаимодействия (*fill*, *click*, *set_input_files*) и проверки (*check_visible*, *heck_have_text*, *check_have_value*, *check_disabled*) выполняются через элементы, а не напрямую через *expect* или *page.locator*.
- Логика компонентов и страниц сохранена:
    - *CoursesListToolbarViewComponent* использует *Text*, *Button*.
    - *CreateCourseExercisesToolbarViewComponent* использует *Text*, *Button*.
    - *CreateCourseFormComponent* использует *Input*, *Textarea*.
    - *CreateCourseToolbarViewComponent* использует *Text*, *Button*.
-   - В коде компонентов и страниц нет прямых вызовов:
    - *page.get_by_test_id(...)*
    - *page.locator(...)*
    - *expect(...)*
    - Всё инкапсулировано в элементах.
- После рефакторинга автотесты запускаются командой:
    ```sh
    python -m pytest -m "regression" -s -v
    ```
                  
и проходят успешно.
- Код чистый, структурированный, соответствует принципам **Page Object + Page Factory**, без дублирования и «сырых» локаторов.
- Соблюдены принципы **PEP8** (отступы, названия переменных, длина строк).

[вверх](#практикуемся-в-применении-page-factory)


## Результат

```sh
vscode@4e841e8a86bd:~/workspace$ source ./run_flake8.sh 
vscode@4e841e8a86bd:~/workspace$ pytest -s -v -m 'regression'
============================ test session starts ===============================
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

============================ 7 passed, 45 deselected in 59.22s =================
```

[вверх](#практикуемся-в-применении-page-factory)