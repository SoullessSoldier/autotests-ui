# 8.5 Добавление видео в Allure отчет
[назад](../readme.md)

## Запись видео в Playwright

Ссылки:
    - [Официальная документация Playwright по работе с видео](https://playwright.dev/python/docs/videos)
Для записи видео во время выполнения автотестов с использованием Playwright достаточно указать директорию, в которую будут сохраняться видеозаписи:
```python
context = browser.new_context(record_video_dir='./videos')
```

Теперь добавим запись видео в фикстуры *chromium_page* и *chromium_page_with_state*.
```python
@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Указываем директорию для сохранения видеозаписей
    context = browser.new_context(record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
```

### Запуск автотестов
Теперь давайте запустим автотесты:
```sh
python -m pytest -m "regression" --alluredir=./allure-results
```
После выполнения тестов в корневой директории проекта *autotests-ui* появится папка *videos*, содержащая файлы видеозаписей.  
Пример содержимого папки:
```
.
└── videos/
    ├── 4bd001a3e24d4d0006a34593ad7f3638.webm
    ├── 8d52eb678338429212bbeb3547ed8004.webm
    ├── 8ee47db4bc4e46b19ccb118cb27f7401.webm
    ├── 780bf980839fc809c7bc62445955ddaf.webm
    ├── d9e981060ba8fb65df52911d1f156fb8.webm
    └── ...
```
Эти файлы представляют собой видеозаписи тестов в формате *.webm*, которые можно открыть для просмотра в браузере.

### Зачем нужна запись видео, если есть Playwright Trace Viewer?
Хоть **Playwright Trace Viewer** и предоставляет мощные инструменты для детального анализа автотестов, иногда удобнее и быстрее воспользоваться видеозаписями. Например, если тестируемое приложение полностью сломалось (например, упал сервер и все тесты не прошли), вам не нужно тратить время на генерацию и открытие отчетов Playwright Trace Viewer. Достаточно быстро просмотреть видео 3-4 тестов, чтобы понять, что все они завершились с одной и той же ошибкой, что сократит время на анализ проблемы.

Тем не менее, Playwright Trace Viewer остается незаменимым инструментом для глубокого анализа и детальной отладки автотестов. Видео помогает для быстрого обзора, но Trace Viewer предоставляет более детальные данные, необходимые для решения сложных проблем.

[вверх](#85-добавление-видео-в-allure-отчет)


## Прикрепление видео в Allure отчет

Ссылки:
    - [Официальная документация, как прикрепить файл к Allure отчету](https://allurereport.org/docs/pytest/#attach-screenshots-and-other-files)

Теперь давайте добавим прикрепление видео в Allure отчет. Это можно сделать по аналогии с тем, как мы прикрепляли отчет Playwright Trace Viewer. Видео можно прикрепить, используя *allure.attach.file()* и указав путь к видеофайлу, который был записан для каждого теста.

### Фикстура chromium_page
Пример с фикстурой chromium_page
```python
@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # Перенесли инициализацию страницы в отдельную переменную
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # Прикрепляем видео автотеста к Allure отчету
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
```

#### Разбор изменений:
1. Инициализация страницы:
    - Мы вынесли page = context.new_page() в отдельную переменную, чтобы получить доступ к пути видеозаписи.
2. Прикрепление видео:
    - *page.video.path()*: Возвращает путь к видеозаписи, которая создается для каждого теста.
    - *allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)*: Мы используем эту строку для прикрепления видео к Allure отчету с указанием, что формат видео — это *WEBM*.

### Запуск автотестов и просмотр отчета
Запускаем автотесты:
```sh
python -m pytest -m "regression" --alluredir=./allure-results
```
                  
Генерируем Allure отчет:
```sh
allure serve ./allure-results
```                  
После завершения автотестов в Allure отчете вы увидите прикрепленные видео тестов в блоке "Tear down" для каждой фикстуры. Видео можно просмотреть прямо в Allure отчете или скачать для анализа.

[вверх](#85-добавление-видео-в-allure-отчет)


## Рефакторинг фикстур chromium_page и chromium_page_with_state

Как можно заметить, после добавления сбора Playwright трейсинга и видео, у нас получились почти идентичные фикстуры.

### Вынесение общей логики
Чтобы избежать дублирования кода, можно создать общую функцию *initialize_playwright_page*, которая будет принимать параметр *storage_state*, чтобы управлять состоянием браузера.

Создадим папку *tools/playwright* и в ней файл *pages.py*, а в нем функцию *initialize_playwright_page*:
```
.
└── tools/
    ├── __init__.py
    └── playwright/
        ├── __init__.py
        └── pages.py
```

В этой функции мы вынесли общую логику для инициализации браузера, трейсинга и видеофиксации. Единственное различие теперь — это параметр storage_state, который по умолчанию равен None. Если он передан, то контекст будет использовать сохраненное состояние, иначе — нет.

### Результат
Использование функции *initialize_playwright_page* позволило значительно сократить и упростить код фикстур. Это улучшает читаемость и упрощает поддержку, так как все общие настройки теперь вынесены в одну функцию. Если в будущем потребуется изменить логику инициализации страницы, это можно сделать в одном месте.

[вверх](#85-добавление-видео-в-allure-отчет)