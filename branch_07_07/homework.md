# Практикуемся в написании автотестов с использованием Page Object, Page Component, Page Factory
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Результат](#результат)

## Задание
В этом задании вам необходимо самостоятельно написать автотест *test_edit_course*, который будет выполнять следующие шаги:
1. Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
2. Заполнить форму создания курса валидными данными, загрузить изображение и нажать кнопку создания курса.
3. Проверить, что на странице https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses отображается карточка ранее созданного курса.
4. Через меню карточки курса нажать на кнопку "Edit".
5. Изменить поля: title, estimated time, description, max score, min score и нажать на кнопку сохранения изменений.
6. Проверить, что на странице https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses отображается карточка курса с обновленными данными.

Автотест *test_edit_course* должен находиться в тестовом классе *TestCourses* и запускаться успешно следующей командой:
```sh
python -m pytest -k "test_edit_course"
```

### Критерии успешного выполнения
- Автотест *test_edit_course* реализован в файле *tests/courses/test_courses.py* в составе класса *TestCourses*.
- Для навигации и действий используются **Page Object / Page Component / Page Factory** классы (*CoursesListPage*, *CreateCoursePage*, компоненты форм, тулбаров, меню и т.д.), а не «сырые» локаторы.
- Шаги теста реализованы последовательно:
    1. Переход на страницу создания курса.
    2. Заполнение формы валидными данными.
    3. Загрузка изображения через *ImageUploadWidgetComponent*.
    4. Нажатие на кнопку создания курса.
    5. Проверка, что на странице списка курсов появилась карточка созданного курса.
    6. Переход в режим редактирования через меню карточки.
    7. Изменение всех полей формы (title, estimated time, description, max score, min score).
    8. Сохранение изменений.
    9. Проверка, что карточка курса обновилась и отображает новые данные.
- Проверки корректности выполняются через методы компонентов (*check_visible*, *check_have_value*, *click_create_course_button*, *click_edit*) и не содержат прямых вызовов expect или page.locator.
- Проверки изменений охватывают **все поля**, которые редактировались (title, estimated time, description, max score, min score).
- Автотест запускается командой и проходит успешно.
    ```sh
    python -m pytest -k "test_edit_course"
    ```
- Код написан чисто и аккуратно, без дублирования, соответствует принципам **Page Object + Page Factory**.
- Соблюдены принципы PEP8 (отступы, названия переменных, длина строк).

[вверх](#практикуемся-в-написании-автотестов-с-использованием-page-object-page-component-page-factory)


## Результат
```sh
vscode@b81db10b4fd2:~/workspace$ source ./run_flake8.sh 
vscode@b81db10b4fd2:~/workspace$ pytest -k "test_edit_course"
============================ test session starts ===============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 55 items / 54 deselected / 1 selected 

tests/courses/test_courses.py::TestCourses::test_edit_course PASSED

============================ 1 passed, 54 deselected in 11.22s =================
```

```sh
vscode@b81db10b4fd2:~/workspace$ pytest -m 'regression'
============================ test session starts ===============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
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

============================ 10 passed, 45 deselected in 46.10s ================
```

[вверх](#практикуемся-в-написании-автотестов-с-использованием-page-object-page-component-page-factory)