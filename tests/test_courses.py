"""Модуль автотеста."""
from pages.courses_list_page import (CheckVisibleCourseCardParams,
                                     CoursesListPage)
from pages.create_course_page import CreateCoursePage

from playwright.sync_api import Page, expect

import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    """
    Функция проверки.

    Проверка того, что свежезарегистрированного пользователя
    нет доступных курсов.
    """
    page = chromium_page_with_state

    page.goto('https://nikita-filonov.github.io/qa-automation'
              '-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    no_results_title = page.get_by_test_id('courses-list-empty-'
                                           'view-title-text')
    expect(no_results_title).to_be_visible()
    expect(no_results_title).to_have_text('There is no results')

    view_description = page.get_by_test_id('courses-list-empty-view-'
                                           'description-text')
    expect(view_description).to_be_visible()
    expect(view_description).to_have_text(('Results from the load test '
                                           'pipeline will be displayed here'))


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage,
                       create_course_page: CreateCoursePage):
    """
    Функция проверки.

    Проверка создания курса и отображения его в списке курсов.
    """
    create_course_page.visit('https://nikita-filonov.github.io/'
                             'qa-automation-engineer-ui-course/#/'
                             'courses/create')

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(
        '',
        '',
        '',
        '0',
        '0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        'Playwright',
        '2 weeks',
        'Playwright',
        '100',
        '10'
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    params = CheckVisibleCourseCardParams(
        index=0,
        title='Playwright',
        max_score='100',
        min_score='10',
        estimated_time='2 weeks'
        )
    courses_list_page.check_visible_course_card(params=params)
