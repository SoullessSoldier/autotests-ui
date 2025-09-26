# Домашняя работа (Практикуемся в написании компонентов с использованием паттерна PageComponent)
[назад](./readme.md)

Содержание:
- [Задание](#задание)
- [Результат](#результат)

## Задание
В данном задании вам необходимо самостоятельно реализовать следующие компоненты:
- **LoginFormComponent** — должен находиться в папке *components/authentication/login_form_component.py*
- **RegistrationFormComponent** — должен находиться в папке *components/authentication/registration_form_component.py*
- **CreateCourseFormComponent** — должен находиться в папке *components/courses/create_course_form_component.py*
- **CreateCourseToolbarViewComponent** — должен находиться в папке *components/courses/create_course_toolbar_view_component.py*
- **CreateCourseExercisesToolbarViewComponent** — должен находиться в папке *components/courses/create_course_exercises_toolbar_view_component.py*
- **DashboardToolbarViewComponent** — должен находиться в папке *components/dashboard/dashboard_toolbar_view_component.py*
- **ChartViewComponent** — должен находиться в папке *components/charts/chart_view_component.py*

### Требования
После реализации всех компонентов вам необходимо интегрировать их на соответствующие страницы. После интеграции компонентов необходимо удалить локаторы и методы, которые были перенесены в компоненты. Также потребуется переписать соответствующие автотесты с использованием новых компонентов, там, где это возможно или необходимо для повышения читаемости и поддержки тестов.

Для проверки корректности работы автотестов нужно использовать команду:
```sh
python -m pytest -m "regression" -s -v
```
### Описания методов, которые должен содержать каждый компонент
1. LoginFormComponent  
**Методы**:
- *fill(email, password)* — заполняет форму с полями электронной почты и пароля.
- *check_visible(email, password)* — проверяет корректность отображения формы и введённых данных.
2. RegistrationFormComponent  
**Методы**:
- *fill(email, username, password)* — заполняет форму регистрации.
- *check_visible(email, username, password)* — проверяет корректность отображения формы и введённых данных.
3. CreateCourseFormComponent  
**Методы**:
- *fill(title, estimated_time, description, max_score, min_score)* — заполняет форму создания курса.
- *check_visible(title, estimated_time, description, max_score, min_score)* — проверяет корректность отображения формы и валидность данных.
4. CreateCourseToolbarViewComponent  
**Методы**:  
- *check_visible(is_create_course_disabled=True)* — проверяет корректность отображения панели управления. Аргумент is_create_course_disabled может принимать значения True или False.
  Если *is_create_course_disabled=True*, проверяется, что кнопка создания курса недоступна:
    *expect(self.create_course_button).to_be_disabled()*
  Если *is_create_course_disabled=False*, проверяется, что кнопка доступна:
    *expect(self.create_course_button).to_be_enabled()*
  Значение аргумента *is_create_course_disabled* по умолчанию должно быть True.

- *click_create_course_button()* — нажимает на кнопку создания курса.
5. CreateCourseExercisesToolbarViewComponent  
**Методы**:
- *check_visible()* — проверяет корректность отображения панели управления.
- *click_create_exercise_button()* — нажимает на кнопку создания задания.
6. DashboardToolbarViewComponent  
**Методы**:  
- *check_visible()* — проверяет корректность отображения панели управления
7. ChartViewComponent  
- Этот компонент принимает динамические аргументы:
  - *identifier* — значения могут быть students, activities, courses, scores.
  - *chart_type* — значения могут быть bar, line, pie, scatter.
- Локаторы формируются динамически в зависимости от переданных аргументов:
  - *self.title = page.get_by_test_id(f'{identifier}-widget-title-text')*
  - *self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')*
**Методы**:
- *check_visible(title)* — проверяет корректность отображения компонента, включая проверку текста заголовка (title).

    Пример инициализации компонента в конструктора класса страницы:
    ```python
    self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
    self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
    self.students_chart_view = ChartViewComponent(page, "students", "bar")
    ```

### Критерии выполнения задания
1. **Файлы и структура**  
- В проекте реализованы отдельные компоненты:
    - *LoginFormComponent* (/components/authentication/login_form_component.py)
    - *RegistrationFormComponent* (/components/authentication/registration_form_component.py)
    - *CreateCourseFormComponent* (/components/courses/create_course_form_component.py)
    - *CreateCourseToolbarViewComponent* (/components/courses/create_course_toolbar_view_component.py)
    - *CreateCourseExercisesToolbarViewComponent* (/components/courses/create_course_exercises_toolbar_view_component.py)
    - *DashboardToolbarViewComponent* (/components/dashboard/dashboard_toolbar_view_component.py)
    - *ChartViewComponent* (/components/charts/chart_view_component.py)
    - *NavbarComponent*, *SidebarComponent* (/components/navigation/...).
- В страницах используются соответствующие компоненты:
    - *LoginPage* — содержит *LoginFormComponent*.
    - *RegistrationPage* — содержит *RegistrationFormComponent*.
    - *CreateCoursePage* — содержит *NavbarComponent*, *ImageUploadWidgetComponent*, *CreateCourseFormComponent*, *CreateCourseToolbarViewComponent*, *CreateCourseExercisesToolbarViewComponent*, *EmptyViewComponent*.
    - *DashboardPage* — содержит *NavbarComponent*, *SidebarComponent*, *ChartViewComponent* (scores, courses, students, activities), *DashboardToolbarViewComponent*.
    - *CoursesListPage* — содержит *NavbarComponent*, *SidebarComponent*, *CoursesListToolbarViewComponent*, *CourseViewComponent*, *EmptyViewComponent*.

2. **Тесты**
- **Тесты авторизации**
  - Файл *tests/test_authorization.py*.
  - Тест называется *test_wrong_email_or_password_authorization*.
  - Маркировки: *@pytest.mark.authorization* и *@pytest.mark.regression*.
  - Используется *LoginPage* и *LoginFormComponent*.
  - Тест параметризован для разных значений *email/password*.
  - Проверяется отображение алерта *Wrong email or password*.
- **Тесты регистрации**
  - Файл *tests/test_registration.py*.
  - Тест называется *test_successful_registration*.
  - Маркировки: *@pytest.mark.registration* и *@pytest.mark.regression*.
  - Используется *RegistrationPage* и *DashboardPage*.
  - Выполняется переход на страницу регистрации.
  - Заполняется форма регистрации *(email, username, password)*.
  - Нажимается кнопка регистрации.
  - После регистрации проверяется отображение дашборда *(DashboardToolbarViewComponent)*.
- **Тесты дашборда**
  - Файл *tests/test_dashboard.py*.
  - Тест называется *test_dashboard_displaying*.
  - Маркировки: *@pytest.mark.dashboard* и *@pytest.mark.regression*.
  - Используется *DashboardPage*.
  - Проверки:
    - *navbar.check_visible("username")*
    - *sidebar.check_visible()*
    - *dashboard_toolbar_view.check_visible()*
    - графики Scores, Courses, Students, Activities отображаются.
- **Тесты курсов**
  - Файл *tests/test_courses.py*.
  - Тест *test_create_course*:
    - Маркировки: *@pytest.mark.courses* и *@pytest.mark.regression*.
    - Используется *CreateCoursePage* и *CoursesListPage*.
    - Проверяется отображение тулбара, формы курса, блока упражнений.
    - Загружается картинка.
    - Заполняется форма курса.
    - Курс успешно создаётся и появляется в списке курсов.
  - Тест *test_empty_courses_list*:
    - Маркировки: *@pytest.mark.courses* и *@pytest.mark.regression*.
    - Используется *CoursesListPage*.
    - Проверки:
      - *navbar.check_visible("username")*
      - *sidebar.check_visible()*
т     - тулбар списка курсов
      - пустой список курсов (*empty_view*).

3. **Общие критерии качества**  
- В тестах используются только Page Object Model и компоненты. Нет «сырых» селекторов.
- Используются стабильные селекторы (по *data-test-id*).
- Нет sleep и лишних ожиданий.
- Код чистый, аккуратный, соответствует PEP8 (названия переменных, длина строк, отступы).
- Тесты запускаются командами:
  ```sh
  python -m pytest -k "test_wrong_email_or_password_authorization" -s -v
  python -m pytest -k "test_successful_registration" -s -v
  python -m pytest -k "test_dashboard_displaying" -s -v
  python -m pytest -k "test_create_course" -s -v
  python -m pytest -k "test_empty_courses_list" -s -v
  ```

[вверх](#домашняя-работа-практикуемся-в-написании-компонентов-с-использованием-паттерна-pagecomponent)


## Результат
```sh
vscode@03d2c5a06c02:~/workspace$ source ./run_flake8.sh 
vscode@03d2c5a06c02:~/workspace$ pytest -s -v -m 'regression'
========================= test session starts ==================================
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

========================= 7 passed, 45 deselected in 24.99s ====================
```
```sh
vscode@03d2c5a06c02:~/workspace$ pytest -k "test_wrong_email_or_password_authorization" -s -v
========================= test session starts ==================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 49 deselected / 3 selected  

tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-password] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[user.name@gmail.com-  ] PASSED
tests/test_authorization.py::test_wrong_email_or_password_authorization[  -password] PASSED

========================= 3 passed, 49 deselected in 8.42s =====================
```
```sh
vscode@03d2c5a06c02:~/workspace$ pytest -k "test_successful_registration" -s -v              
========================= test session starts ==================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected    

tests/test_registration.py::test_successful_registration PASSED

========================= 1 passed, 51 deselected in 3.94s =====================
```
```sh
vscode@03d2c5a06c02:~/workspace$ pytest -k "test_dashboard_displaying" -s -v
========================= test session starts ==================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected 

tests/test_dashboard.py::test_dashboard_displaying PASSED

========================= 1 passed, 51 deselected in 6.12s =====================
```
```sh
vscode@03d2c5a06c02:~/workspace$ pytest -k "test_create_course" -s -v
========================= test session starts ==================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected  

tests/test_courses.py::test_create_course PASSED

========================= 1 passed, 51 deselected in 8.87s =====================
```
```sh
vscode@03d2c5a06c02:~/workspace$ pytest -k "test_empty_courses_list" -s -v
========================= test session starts ==================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected

tests/test_courses.py::test_empty_courses_list PASSED

========================= 1 passed, 51 deselected in 6.07s =====================
```
[вверх](#домашняя-работа-практикуемся-в-написании-компонентов-с-использованием-паттерна-pagecomponent)
