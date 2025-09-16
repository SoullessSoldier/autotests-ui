# Практикуемся в написании автотестов с использованием POM
[назад](./readme.md)

Файлы:
- *./fixtures/pages.py* - добавлены фикстуры *courses_list_page*, *courses_list_page*
- *./pages/dashboard_page.py* - Класс POM страницы дашборда
- *./pages/create_course_page.py* - Класс POM страницы создания курса
- *./pages/courses_list_page.py* - класс POM страницы списка курсов
- *./testdata/files/image.png* - файл тестового изображения курса
- *./tests/test_courses.py* - добавлен тест *test_create_course*

Содержание
- [Шаги автотеста](#шаги-автотеста)
- [Критерии выполнения задания](#критерии-выполнения-задания)
- [Результат](#результат)


В данном задании вам предстоит самостоятельно реализовать автотест test_create_course с использованием страниц CoursesListPage и CreateCoursePage, которые мы рассмотрели на уроке. Автотест должен находиться в файле test_courses.py и быть помечен маркировками courses и regression для pytest.

## Шаги автотеста:
1. Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
2. Проверить наличие заголовка "Create course" с помощью метода *check_visible_create_course_title*.
3. Проверить, что кнопка создания курса недоступна для нажатия — метод *check_disabled_create_course_button*.
4. Убедиться, что отображается пустой блок для предпросмотра изображения — метод *check_visible_image_preview_empty_view*.
5. Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана — метод *check_visible_image_upload_view*.
6. Проверить, что форма создания курса отображается и содержит значения по умолчанию. Поля *title*, *description*, *estimated_time* должны быть пустыми строками, а для полей *max_score* и *min_score* установлены значения "0" — метод *check_visible_create_course_form*.
7. Проверить наличие заголовка "Exercises" — метод *check_visible_exercises_title*.
8. Проверить наличие кнопки создания задания — метод *check_visible_create_exercise_button*.
9. Убедиться, что отображается блок с пустыми заданиями — метод *check_visible_exercises_empty_view*.
10. Загрузить изображение для превью курса. Для этого необходимо добавить картинку в проект:
  - Создайте папку *testdata* в корне проекта *autotests-ui*.
  - Внутри папки *testdata* создайте папку *files*.
  - Положите в папку *files* любое изображение формата .png и назовите его *image.png*, чтобы структура проекта выглядела следующим образом:
    ```
        .
        └── testdata/
            └── files/
                └── image.png
    ```
                  
  - Передайте путь к файлу *./testdata/files/image.png* в метод загрузки изображения — метод *upload_preview_image*.
11. Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена — метод *check_visible_image_upload_view*.
12. Заполнить форму создания курса значениями:
  - title = "Playwright",
  - estimated_time = "2 weeks",
  - description = "Playwright",
  - max_score = "100",
  - min_score = "10". Для заполнения формы используйте метод *fill_create_course_form*.
13. Нажать на кнопку создания курса — метод *click_create_course_button*.
14. После создания курса произойдет редирект на страницу со списком курсов. Необходимо проверить наличие заголовка "Courses" — метод *check_visible_courses_title*.
15. Проверить наличие кнопки создания курса — метод *check_visible_create_course_button*.
16. Проверить корректность отображаемых данных на карточке курса — метод *check_visible_course_card*.


Тех страниц и методов, которые мы реализовали, вполне достаточно для создания автотеста. Вам не нужно модифицировать POM или добавлять новые методы для выполнения этого задания.

В итоге у вас должен получиться автотест *test_create_course*. Чтобы запустить его и убедиться, что тест проходит успешно, используйте следующую команду:
```sh
python -m pytest -k "test_create_course" -s -v
```

[вверх](#практикуемся-в-написании-автотестов-с-использованием-pom)
                  

## Критерии выполнения задания
- Размещение и маркировки
  - Тест расположен в *tests/test_courses.py*.
  - Тест называется *test_create_course*.
  - У теста есть маркировки: *@pytest.mark.courses* и *@pytest.mark.regression*.
- Использование POM и фикстур
  - В тесте используются только страницы *CreateCoursePage* и *CoursesListPage* через готовые фикстуры (например, *create_course_page*, *courses_list_page*).
  - В тесте нет “сырых” селекторов и прямой работы с page.
  - POM/методы **не модифицируются** и не дописываются — используются как в уроке.
- Подготовка тестовых данных
  - В проекте создан файл изображения по пути: *./testdata/files/image.png*
- Пошаговые проверки на странице Create Course
  - Открывается страница *#/courses/create*.
  - Проверен заголовок "Create course" — *check_visible_create_course_title*.
  - Проверено, что кнопка создания курса disabled — *check_disabled_create_course_button*.
  - Проверен пустой предпросмотр изображения — *check_visible_image_preview_empty_view*.
  - Проверен блок загрузки изображения в состоянии без выбранной картинки — *check_visible_image_upload_view(is_image_uploaded=False)*.
  - Проверена форма со значениями по умолчанию (*title=""*, *description=""*, *estimated_time=""*, *max_score="0"*, *min_score="0"*) — *check_visible_create_course_form*.
  - Проверен заголовок "Exercises" — *check_visible_exercises_title*.
  - Проверена кнопка создания задания — check_visible_create_exercise_button*.
  - Проверен пустой блок заданий — *check_visible_exercises_empty_view*.
- Действия по созданию курса
  - Загружено изображение *./testdata/files/image.png* — *upload_preview_image*.
  - Проверен блок загрузки в состоянии после успешной загрузки — *check_visible_image_upload_view(is_image_uploaded=True)*.
  - Форма заполнена значениями:
    - *title="Playwright"*, *estimated_time="2 weeks"*, *description="Playwright"*, *max_score="100"*, *min_score="10"* — *fill_create_course_form*.
  - Нажата кнопка создания курса — click_create_course_button.
- Проверки после редиректа на Courses
  - Проверен заголовок "Courses" — *check_visible_courses_title*.
  - Проверена кнопка создания курса — *check_visible_create_course_button*.
  - Проверена карточка созданного курса (как минимум *title*, *max_score*, *min_score*, *estimated_time*) — *check_visible_course_card*.
- Запуск и качество реализации
  - Тест успешно проходит командой:
    ```sh
    python -m pytest -k "test_create_course" -s -v
    ```
  - Используются стабильные селекторы (по data-test-id в POM).
  - Нет sleep/магических задержек; полагаемся на ожидания внутри POM.
  - Код аккуратный, читабельный, соответствует PEP8.

[вверх](#практикуемся-в-написании-автотестов-с-использованием-pom)


## Результат
```sh
vscode@caef0fcb72c3:~/workspace$ flake8 --per-file-ignores="__init__.py:D104" ./fixtures
vscode@caef0fcb72c3:~/workspace$ flake8 --per-file-ignores="__init__.py:D104" ./pages   
vscode@caef0fcb72c3:~/workspace$ flake8 ./tests/test_courses.py 
vscode@caef0fcb72c3:~/workspace$ pytest -s -v -k 'test_create_course'
======================= test session starts ====================================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/vscode/workspace
configfile: pytest.ini
plugins: rerunfailures-16.0.1, base-url-2.1.0, allure-pytest-2.15.0, playwright-0.7.1
collected 51 items / 50 deselected / 1 selected  
tests/test_courses.py::test_create_course PASSED

======================= 1 passed, 50 deselected in 7.71s =======================
```

[вверх](#практикуемся-в-написании-автотестов-с-использованием-pom)