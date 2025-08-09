# 5.6 Работа с авторизацией в Playwright
[назад](../readme.md)

Сохранение состояния браузера, использование сохраненного состояние браузера
Файл ./src/playwright_registration.py

## Практика работы с авторизацией в Playwright
В данном задании вам необходимо объединить механизм регистрации и открытия новой страницы  
с сохраненным состоянием, скрипт должен делать следующие действия:
- Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
- Заполнить форму регистрации и нажать на кнопку "Registration"
- Сохранить состояние браузера
- Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
- Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
- Проверить наличие и текст заголовка "Courses" 
- Проверить наличие и текст блока "There is no results"
- Файл со скриптом должен называться: playwright_courses.py  



Ссылки:
- [Документация по localStorage](https://developer.mozilla.org/ru/docs/Web/API/Window/localStorage)
- [Документация по sessionStorage](https://developer.mozilla.org/ru/docs/Web/API/Window/sessionStorage)
- [Документация по HTTP-cookies](https://developer.mozilla.org/ru/docs/Web/HTTP/Guides/Cookies)

