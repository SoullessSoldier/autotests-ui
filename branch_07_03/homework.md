# Практика работы с Page Component
[назад](./readme.md)

Содержание
- [Добавление компонента SidebarComponent на страницы CoursesListPage и DashboardPage](#1-добавление-компонента-sidebarcomponent-на-страницы-courseslistpage-и-dashboardpage)
- [Добавление компонента NavbarComponent на страницу CoursesListPage](#2-добавление-компонента-navbarcomponent-на-страницу-courseslistpage)
- [Использование компонентов в автотестах test_dashboard_displaying и test_empty_courses_list](#3-использование-компонентов-в-автотестах-test_dashboard_displaying-и-test_empty_courses_list)
- [Результат](#результат)

В этом задании вам предстоит самостоятельно интегрировать компоненты *NavbarComponent*, *SidebarComponent* в автотесты *test_dashboard_displaying* и *test_empty_courses_list*.

Задание состоит из трех этапов:
- Добавление компонента *SidebarComponent* на страницы *CoursesListPage* и *DashboardPage*.
- Добавление компонента *NavbarComponent* на страницу *CoursesListPage*.
- Использование компонента в автотестах *test_dashboard_displaying* и *test_empty_courses_list*

## 1. Добавление компонента *SidebarComponent* на страницы *CoursesListPage* и *DashboardPage*
Компонент *SidebarComponent* необходимо добавить в конструкторы классов страниц *CoursesListPage* и *DashboardPage* как атрибут *sidebar*. Это делается следующим образом:
```python
self.sidebar = SidebarComponent(page)
```
## 2. Добавление компонента *NavbarComponent* на страницу *CoursesListPage*
Компонент *NavbarComponent* необходимо добавить в конструктор класса страницы *CoursesListPage* как атрибут *navbar*.  
Это делается следующим образом:
```python
self.navbar = NavbarComponent(page)
```
## 3. Использование компонентов в автотестах *test_dashboard_displaying* и *test_empty_courses_list*
- **Автотест** *test_dashboard_displaying*

    В этом автотесте вам нужно добавить проверку корректного отображения компонента *Sidebar* в начале теста, используя ранее реализованный компонент *SidebarComponent*. Убедитесь, что перед этим вы добавили компонент *SidebarComponent* в конструктор страницы *DashboardPage*.

    Тест должен запускаться командой и успешно проходить:
    ```sh
    python -m pytest -k "test_dashboard_displaying" -s -v
    ```
- **Автотест** *test_empty_courses_list*
    Этот автотест требует чуть более сложной работы, так как он еще не переписан с использованием паттерна Page Object Model (POM). Однако у нас уже есть страница CoursesListPage, которую можно использовать для переписывания теста.
    
    В итоге автотест *test_empty_courses_list* должен проверять следующие элементы:
    - **Отображение компонента Navbar** — проверяет, что компонент Navbar корректно отображается на странице.
    - **Отображение компонента Sidebar** — проверяет, что компонент Sidebar виден и корректно отрисован.
    - **Отображение заголовка "Courses"** — проверяет наличие и корректное отображение заголовка страницы.
    - **Отображение кнопки создания курса** — проверяет, что кнопка для создания нового курса отображается.
    - **Отображение пустого блока с текстом "There is no results"** — проверяет, что при отсутствии курсов отображается соответствующий блок с сообщением об отсутствии результатов.
    
    Тест должен запускаться командой и успешно проходить:
    ```sh
    python -m pytest -k "test_empty_courses_list" -s -v
    ```

[вверх](#практика-работы-с-page-component)


## Результат
```sh
vscode@466db8c282cc:~/workspace$ flake8 --per-file-ignores="__init__.py:D104"
vscode@466db8c282cc:~/workspace$ pytest -k "test_dashboard_displaying" -s -v
========================== test session starts =================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected
tests/test_dashboard.py::test_dashboard_displaying PASSED

========================== 1 passed, 51 deselected in 7.56s ====================
```
```sh
vscode@466db8c282cc:~/workspace$ pytest -k "test_empty_courses_list" -s -v
========================== test session starts =================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 52 items / 51 deselected / 1 selected                                                                                                                                        

tests/test_courses.py::test_empty_courses_list PASSED

========================== 1 passed, 51 deselected in 5.40s ====================
```
[вверх](#практика-работы-с-page-component)
