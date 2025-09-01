"""Модуль автотеста."""
import os

from playwright.sync_api import expect, sync_playwright

import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    """
    Функция проверки.

    Проверка того, что свежезарегистрированного пользователя
    нет доступных курсов.
    """
    src_dir = '/tmp'
    state_path = os.path.join(src_dir, 'browser-state.json')

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation'
                  '-engineer-ui-course/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form'
                                                       '-email-input'
                                                       ).locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form'
                                                          '-username-input'
                                                          ).locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form'
                                                          '-password-input'
                                                          ).locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page'
                                                  '-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()

        context.storage_state(path=state_path)

    with (sync_playwright() as playwright):
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state=state_path)
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation'
                  '-engineer-ui-course/#/courses')

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        no_results_title = page.get_by_test_id('courses-list-empty'
                                               '-view-title-text')
        expect(no_results_title).to_be_visible()
        expect(no_results_title).to_have_text('There is no results')

        view_description = page.get_by_test_id('courses-list-empty'
                                               '-view-description-text')
        expect(view_description).to_be_visible()
        expect(view_description).to_have_text('Results from the load test '
                                              'pipeline will be '
                                              'displayed here')
