# Stepik - Автоматизация тестирования UI с Python и Playwright
**Автор - Никита Филонов**


### Шаги:
- создан удаленный репозиторий
- создан локальный репозиторий
- доступ к Github по токенам настроен
- для работы с Playwright был собран образ в Докере. Здесь и далее предполагается запуск образа  
с пробросом текущего каталога как volume в ~/workspace
- Работа начинается сразу с модуля 5.4 теории.  
- Начиная с модуля 6.5 тесты размещены в каталоге tests корневого каталога проекта,  
в каталогах веток модлей размещены учебные файлы кода  
- Начиная с модуля 6.6 фикстуры размещены в каталоге fixtures корневого каталога проекта,  
также в корне проекта размещен файл conftest.py, подключающий фикстуры как плагины.
- Начиная с модуля 7.1 докер-контейнер запускается скриптом run_pw2_v2.sh из папки docker с 
подключением родительской папки проекта как volume;  
изменения в тестах вносятся в папках  
*fixtures*, *pages*, *tests*, файлах *conftest.py*, *pytest.ini*

Содержание:  
- **5. Основы автоматизации с Playwright**  
  - [branch_05_04 - Модуль 5.4 "Введение в Playwright"](./branch_05_04/readme.md)
  - [branch_05_05 - Модуль 5.5 "Углубление в Playwright"](./branch_05_05/readme.md)
  - [branch_05_06 - Модуль 5.6 "Работа с авторизацией в Playwright"](./branch_05_06/readme.md)  
- **6. Управление автотестами с Pytest**  
  - [branch_06_02 - Модуль 6.2 "Интеграция Pytest и Playwright"](./branch_06_02/readme.md)
  - [branch_06_03 - Модуль 6.3 "Маркировки Pytest"](./branch_06_03/readme.md)
  - [branch_06_04 - Модуль 6.4 "Pytest skip, skipif, xfail"](./branch_06_04/readme.md)
  - [branch_06_05 - Модуль 6.5 "Фикстуры Pytest"](./branch_06_05/readme.md)
  - [branch_06_06 - Модуль 6.6 "Плагины Pytest"](./branch_06_06/readme.md)
  - [branch_06_07 - Модуль 6.7 "Параметризация Pytest"](./branch_06_07/readme.md)
  - [branch_06_08 - Модуль 6.8 "Перезапуски автотестов в Pytest"](./branch_06_08/readme.md)  
- **7. Паттерны автоматизации тестирования UI**  
  - [branch_07_01 - Модуль 7.1 "Знакомство с PageObject"](./branch_07_01/readme.md)
  - [branch_07_02 - Модуль 7.2 "Практикуемся в реализации PageObject"](./branch_07_02/readme.md)
  - [branch_07_03 - Модуль 7.3 "Знакомство с PageComponent"](./branch_07_03/readme.md)
  - [branch_07_04 - Модуль 7.4 "Практикуемся в реализации PageComponent"](./branch_07_04/readme.md)
  - [branch_07_05 - Модуль 7.5 "Знакомство с PageFactory"](./branch_07_05/readme.md)
  - [branch_07_06 - Модуль 7.6 "Практические применение PageFactory в автотестах"](./branch_07_06/readme.md)
  - [branch_07_07 - Модуль 7.7 "Наращивание тестовой базы и рефакторинг"](./branch_07_07/readme.md)
- **8. Создание Allure отчета**
  - [branch_08_01 - Модуль 8.1 "Знакомство с Allure"](./branch_08_01/readme.md)
  - [branch_08_02 - Модуль 8.2 "Интеграция Allure в автотесты"](./branch_08_02/readme.md)
  - [branch_08_03 - Модуль 8.3 "Добавление Allure шагов в автотесты"](./branch_08_03/readme.md)
  - [branch_08_04 - Модуль 8.4 "Добавление Playwright Trace Viewer в Allure отчет"](./branch_08_04/readme.md)
  - [branch_08_05 - Модуль 8.5 "Добавление видео в Allure отчет"](./branch_08_05/readme.md)
  - [branch_08_06 - Модуль 8.6 "Знакомство с Allure TestOPS"](./branch_08_06/readme.md)
- **9. Улучшение автотестов**
  - [branch_09_01 - Модуль 9.1 "Настройки автотестов с Pydantic"](./branch_09_01/readme.md)
  - [branch_09_02 - Модуль 9.2 "Запуск автотестов на разных браузерах"](./branch_09_02/readme.md)
  - [branch_09_03 - Модуль 9.3 "Параллельный запуск автотестов"](./branch_09_03/readme.md)
  - [branch_09_04 - Модуль 9.4 "Моки и оптимизация UI автотестов"](./branch_09_04/readme.md)
- **Служебное**
  - [docker - Описание изолированной среды в Docker для работы с Playwright](./docker/readme.md)
