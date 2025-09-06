"""Модуль автотеста."""
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
