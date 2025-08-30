"""Модуль автотеста."""
import os

from playwright.sync_api import expect, sync_playwright


def test_empty_courses_list():
    """
    Функция проверки.

    Проверка того, что свежезарегистрированного пользователя
    нет доступных курсов.
    """
    src_dir = '/tmp'
    state_path = os.path.join(src_dir, 'browser-state.json')

    with sync_playwright() as pw:
        url_registration = ('https://nikita-filonov.github.io/qa-automation'
                            '-engineer-ui-course/#/auth/registration')
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url_registration)

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

        url_courses = ('https://nikita-filonov.github.io/qa-automation'
                       '-engineer-ui-course/#/courses')
        page.goto(url_courses)

        courses_title_id = 'courses-list-toolbar-title-text'
        courses_title_text = 'Courses'
        courses_title = page.get_by_test_id(courses_title_id)
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text(courses_title_text)

        empty_icon_id = 'courses-list-empty-view-icon'
        empty_icon = page.get_by_test_id(empty_icon_id)
        expect(empty_icon).to_be_visible()

        no_results_title_id = 'courses-list-empty-view-title-text'
        no_results_title_text = 'There is no results'
        no_results_title = page.get_by_test_id(no_results_title_id)
        expect(no_results_title).to_be_visible()
        expect(no_results_title).to_have_text(no_results_title_text)

        view_description_id = 'courses-list-empty-view-description-text'
        view_description_text = ('Results from the load test pipeline will be '
                                 'displayed here')
        view_description = page.get_by_test_id(view_description_id)
        expect(view_description).to_be_visible()
        expect(view_description).to_have_text(view_description_text)
