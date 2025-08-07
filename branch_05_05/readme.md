# Модуль 5.4 "Углубление в Playwright"
[назад](../readme.md)

- Disabled элементы
- Работа с клавиатурой в Playwright
- Запуск JavaScript-кода на странице
- Наведение мыши (hover) в Playwright
- Работа с событиями в Playwright
- Работа с ошибками при написании автотестов


Файлы ./src/*.py - разбор теории:
- playwright_disabled.py --- поиск disabled-элементов
- playwright_keyboard.py --- работа с клавиатурой
- playwright_js.py --- Запуск JavaScript-кода
- playwright_hover.py --- Наведение мыши (hover) в Playwright
- playwright_events.py --- Работа с событиями в Playwright
- playwright_errors.py --- Работа с ошибками при написании автотестов

Файл ./src/playwright_registration_button.py - задание модуля теории.

### Практика по углубленной работе с Playwright
В данном задании вам необходимо написать скрипт, который выполнит следующие действия:
- Откроет страницу регистрации.
- Проверит, что кнопка "Registration" находится в состоянии disabled.
- Заполнит форму регистрации.
- Убедится, что кнопка "Registration" стала доступной для взаимодействия (enabled).

#### Шаги выполнения скрипта:
- Открыть страницу регистрации: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration.
- Проверить, что кнопка "Registration" находится в состоянии disabled.
- Заполнить поле Email значением: user.name@gmail.com.
- Заполнить поле Username значением: username.
- Заполнить поле Password значением: password.
- Проверить, что кнопка "Registration" перешла в состояние enabled.

#### Требования к скрипту:
- Название файла: *playwright_registration_button.py*.
- Расположение файла: корень проекта *autotests-ui*



Ссылки:
- [Документация по атрибуту disabled в HTML](https://www.w3schools.com/tags/att_disabled.asp)
- [Playwright проверка disabled элемента](https://playwright.dev/python/docs/api/class-locatorassertions#locator-assertions-to-be-disabled)
- [Playwright проверка not disabled элемента](https://playwright.dev/python/docs/api/class-locatorassertions#locator-assertions-not-to-be-disabled)
- [Документация по работе с клавиатурой в Playwright](https://playwright.dev/python/docs/api/class-keyboard)
- [Документация Playwright по запуску JavaScript кода на странице](https://playwright.dev/python/docs/evaluating)
- [Документация по выполнению наведения в Playwright](https://playwright.dev/python/docs/api/class-locator#locator-hover)
- [Документация по работе с мышью в Playwright](https://playwright.dev/python/docs/api/class-mouse)
- [Документация по работе с событиями на странице в Playwright](https://playwright.dev/python/docs/events)


