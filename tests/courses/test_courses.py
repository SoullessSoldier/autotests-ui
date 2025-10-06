"""Модуль автотеста."""
from dataclasses import asdict

import allure

from allure_commons.types import Severity

from pages.courses.courses_list_page import (CheckVisibleCourseCardParams,
                                             CoursesListPage)
from pages.courses.create_course_page import CreateCoursePage

import pytest

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    """Класс тестов курсов."""

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        """
        Функция проверки.

        Проверка того, что у свежезарегистрированного пользователя
        нет доступных курсов.
        """
        courses_list_page.visit('https://nikita-filonov.github.io/'
                                'qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('username')

        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.empty_view.\
            check_visible(
                title='There is no results',
                description=('Results from the load test pipeline '
                             'will be displayed here')
                             )

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage,
                           create_course_page: CreateCoursePage):
        """
        Функция проверки.

        Проверка создания курса и отображения его в списке курсов.
        """
        create_course_page.visit('https://nikita-filonov.github.io/'
                                 'qa-automation-engineer-ui-course/#/'
                                 'courses/create')

        create_course_page.create_course_toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=False
        )
        create_course_page.create_course_form.check_visible(title='',
                                                            estimated_time='',
                                                            description='',
                                                            max_score='0',
                                                            min_score='0')
        create_course_page.create_exercises_toolbar.check_visible()
        create_course_page.exercises_empty_view.check_visible(
                title='There is no exercises',
                description=('Click on "Create exercise" button to '
                             'create new exercise')
            )

        create_course_page.image_upload_widget\
            .upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=True
        )

        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()

        params = CheckVisibleCourseCardParams(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
            )
        courses_list_page.course_view.check_visible(**asdict(params))

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(
            self,
            courses_list_page: CoursesListPage,
            create_course_page: CreateCoursePage
    ):
        """Метод проверяет корректность функц-ла изменения карточки курса."""
        create_course_page.visit('https://nikita-filonov.github.io/'
                                 'qa-automation-engineer-ui-course/#/'
                                 'courses/create')

        create_course_page.create_course_toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=False
        )
        create_course_page.create_course_form.check_visible(title='',
                                                            estimated_time='',
                                                            description='',
                                                            max_score='0',
                                                            min_score='0')
        create_course_page.create_exercises_toolbar.check_visible()
        create_course_page.exercises_empty_view.check_visible(
                title='There is no exercises',
                description=('Click on "Create exercise" button to '
                             'create new exercise')
            )

        # Заполнение исходными данными
        create_course_page.image_upload_widget\
            .upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=True
        )

        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        # Проверка, что в карточке сохранены исходные данные
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        )

        # Изменение карточки курса
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(
            title='New Playwright',
            estimated_time='3 weeks',
            description='New Playwright',
            max_score='1000',
            min_score='100'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        # Проверка, что в карточке сохранены новые данные
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='New Playwright',
            estimated_time='3 weeks',
            max_score='1000',
            min_score='100'
        )
