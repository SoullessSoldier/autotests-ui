# Практика работы с *allure.step*
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Результат](#результат)

## Задание
В этом задании вам необходимо самостоятельно написать allure шаги для следующих компонентов, опираясь на примеры и рекомендации, которые мы рассмотрели в этом уроке.

Компоненты:
- *ChartViewComponent*
- *CoursesListToolbarViewComponent*
- *CreateCourseExercisesToolbarViewComponent*
- *CreateCourseFormComponent*
- *CreateCourseToolbarViewComponent*
- *DashboardToolbarViewComponent*
- *NavbarComponent*

### Критерии успешного выполнения
1. **Добавлены *@allure.step* во все указанные компоненты**:
    - *ChartViewComponent*
    - *CoursesListToolbarViewComponent*
    - *CreateCourseExercisesToolbarViewComponent*
    - *CreateCourseFormComponent*
    - *CreateCourseToolbarViewComponent*
    - *DashboardToolbarViewComponent*
    - *NavbarComponent*
2. **Каждый метод проверки (*check_visible*, *fill*) обернут в *@allure.step*:**
    - Формулировка шага должна быть информативной и соответствовать назначению метода: например, "Check visible chart view \"{title}\"", "Fill create course form", "Check visible navbar".
    - В шагах, где есть параметры, они должны быть выведены в текст шага ({title}, {username}, {index} и т.д.).
3. **Клики (click_*) не оборачиваются в дополнительные шаги.** Это важно: внутри элементов Button, Link, Input уже есть встроенные allure.step благодаря Page Factory. Повторное добавление шагов привело бы к дублированию.
4. **Методы проверки значений используют параметры:**
    - Если метод работает с текстом или значением поля, *allure.ste* должен содержать этот параметр в описании.
    - Например, *"Check visible course view at index \"{index}\""* или *"Check visible navbar for user \"{username}\""*.
5. **Один метод = один allure.step.**
    - Если метод выполняет сразу несколько разных проверок (например, *check_visible* для нескольких полей), шаг остаётся один, но внутри него последовательно вызываются проверки элементов.
    - Если метод делает принципиально разные действия (например, проверка и заполнение), они разделяются на отдельные методы с разными шагами (*check_visible* vs *fill*).
6. **Нет дублирования шагов.**
    - Методы, которые лишь вызывают другой метод (например, *click_create_course_button* → *self.create_course_button.click()*), не получают отдельный *@allure.step*.
    - В отчёте остаются только уникальные и информативные шаги.
7. **Читаемость отчёта.**
    - Все шаги отображаются в Allure как осмысленные действия пользователя: "Check visible…", "Fill…".
    - В отчёте по тесту должно быть легко понять, что именно проверялось или заполнялось.

[вверх](#практика-работы-с-allurestep)

## Результат
```sh
vscode@7ca23ad60356:~/workspace$ source ./run_flake8.sh 
vscode@7ca23ad60356:~/workspace$ source ./run_pytest_allure_report.sh 
========================== test session starts =================================
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

========================== 10 passed, 45 deselected in 59.58s ==================
--output=./allure-report does not exist
Report successfully generated to allure-report
```
[вверх](#практика-работы-с-allurestep)
