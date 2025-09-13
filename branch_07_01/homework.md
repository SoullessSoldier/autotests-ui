# Практика работы с Page Object
[назад](./readme.md)

Содержание
- [Цели задания](#цели-задания)
- [Шаги выполнения задания](#шаги-выполнения-задания)
- [Критерии выполнения задания](#критерии-выполнения-задания)

В этом задании вам предстоит самостоятельно реализовать страницу **RegistrationPage** на основе сайта https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration, используя паттерн **Page Object Model (POM)**. В качестве примера для реализации вы можете воспользоваться страницей **LoginPage**.

## Цели задания:
Практика создания и работы с Page Object Model.
Освоение принципов организации кода с использованием фикстур.
Навыки повторного использования кода и повышения его читабельности.

## Шаги выполнения задания:
1. Создайте страницу **RegistrationPage**:
    - Реализуйте класс **RegistrationPage** в файле *registration_page.py*, используя паттерн POM по аналогии с **LoginPage**.
    - Все методы и локаторы должны быть описаны в соответствии со стандартом именования методов:  
      *{action}_{context}_{element_type}*, где:
        - *action* — действие (например, click, fill).
        - *context* — контекст (например, registration_form).
        - *element_type* — тип элемента (например, button, input).

2. **Создайте фикстуру для RegistrationPage**:
    - В файле *fixtures/pages.py* добавьте фикстуру для инициализации страницы **RegistrationPage**.
    - Фикстура должна иметь function-область видимости, так как каждый тест должен получать новый экземпляр страницы.

3. **Примените страницу RegistrationPage в автотесте**:
    - Воспользуйтесь фикстурой **RegistrationPage** в автотесте *test_successful_registration*, чтобы протестировать успешную регистрацию пользователя на сайте.

4. **Опишите страницу Dashboard**:
    - Так как в автотесте используется проверка заголовка на странице "Dashboard", вам нужно создать отдельную страницу **DashboardPage**.
    - Достаточно описать один локатор и один метод для проверки видимости заголовка "Dashboard". Пример кода для проверки заголовка:
      ```
      self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
      ...
      expect(self.dashboard_title).to_be_visible()
     ```

5. **Создайте фикстуру для DashboardPage**:
    - Реализуйте фикстуру для инициализации **DashboardPage** в файле *fixtures/pages.py*.

[вверх](#практика-работы-с-page-object)


## Критерии выполнения задания
- **Структура проекта**
  - Созданы файлы страниц:
    - *pages/registration_page.py* — Page Object для страницы регистрации.
    - *pages/dashboard_page.py* — Page Object для Dashboard (один локатор заголовка и метод проверки).
  - Создан файл с фикстурами страниц: *fixtures/pages.py*, где объявлены фикстуры:
    - *registration_page* → возвращает *RegistrationPage*.
    - *dashboard_page* → возвращает *DashboardPage*.
- **RegistrationPage (POM)**
  - Реализован класс *RegistrationPage* с локаторами и методами для регистрации.
  - Есть метод для **заполнения формы регистрации** и метод для **нажатия на кнопку регистрации**.
  - Именование методов/локаторов соответствует соглашению *{action}_{context}_{element_type}* (например, *fill_registration_form*, *click_registration_button*).
  - Локаторы стабильные (по *data-test-id*).
- **DashboardPage (POM)**
  - Реализован класс *DashboardPage* с локатором заголовка **Dashboard**.
  - Реализован метод, который проверяет **видимость и текст заголовка** "Dashboard".
- **Фикстуры страниц** (в *fixtures/pages.py*)
  - Фикстуры *registration_page* и *dashboard_page* имеют область видимости **function**.
  - Фикстуры возвращают готовые объекты POM и используют предоставленную **Page** (из базовой браузерной фикстуры проекта).
- **Автотест** *test_successful_registration*
  - Находится в *tests/test_registration.py*.
  - Использует **только POM** через фикстуры: *registration_page*, *dashboard_page* (без “сырых” селекторов и прямой работы с *page*).
  - Сценарий теста:
    1. переход на страницу регистрации;
    2. заполнение формы (email/username/password);
    3. клик по кнопке регистрации;
    4. проверка на Dashboard видимости и текста заголовка "**Dashboard**".
  - У теста **обязательны** маркировки: *@pytest.mark.registration* и *@pytest.mark.regression*.
  - Тест запускается и проходит без ошибок.
- **Качество реализации**
  - Стабильные селекторы (*data-test-id*), без *sleep*.
  - POM инкапсулирует локаторы/логику; в тесте нет дублирования селекторов.
  - Код аккуратный, соблюдён PEP8. 

[вверх](#практика-работы-с-page-object)


## Результат
```sh
vscode@f9d1297493e7:~/workspace$ flake8 ./tests/test_successful_registration.py 
vscode@f9d1297493e7:~/workspace$ pytest -s -v -k 'registration'
====================== test session starts =====================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 50 items / 49 deselected / 1 selected                                              

tests/test_successful_registration.py::test_successful_registration PASSED

====================== 1 passed, 49 deselected in 4.19s ========================
```
[вверх](#практика-работы-с-page-object)