"""Модуль автотеста."""
import os

from playwright.sync_api import expect, sync_playwright

SRC_DIR = '/tmp/'
STORAGE_PATH = os.path.join(SRC_DIR, 'browser-state.json')
URL_REGISTRATION = ('https://nikita-filonov.github.io/'
                    'qa-automation-engineer-ui-course/'
                    '#/auth/registration')
URL_DASHBOARD = ('https://nikita-filonov.github.io/'
                 'qa-automation-engineer-ui-course/#/dashboard')


def test_successful_registration():
    """
    Функция проверки.

    Регистрация нового пользователя и успешный вход.
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()
        page.goto(URL_REGISTRATION)

        reg_email_input_id = 'registration-form-email-input'
        reg_email_value = 'user.name@gmail.com'
        registration_email_input = page.get_by_test_id(reg_email_input_id
                                                       ).locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill(reg_email_value)

        reg_username_input_id = 'registration-form-username-input'
        reg_username_value = 'username'
        registration_username_input = page.get_by_test_id(reg_username_input_id
                                                          ).locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill(reg_username_value)

        reg_password_input_id = 'registration-form-password-input'
        reg_password_value = 'password'
        registration_password_input = page.get_by_test_id(reg_password_input_id
                                                          ).locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill(reg_password_value)

        reg_btn_id = 'registration-page-registration-button'
        registration_button = page.get_by_test_id(reg_btn_id)
        expect(registration_button).to_be_visible()
        registration_button.click()

        context.storage_state(path=STORAGE_PATH)

    # Второй прогон с использованием сохраненного состояния,
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STORAGE_PATH)
        page = context.new_page()
        page.goto(URL_DASHBOARD)

        dashboard_toolbar_id = 'dashboard-toolbar-title-text'
        dashboard_toolbar_text = 'Dashboard'
        dashboard_toolbar_title = page.get_by_test_id(dashboard_toolbar_id)
        expect(dashboard_toolbar_title).to_be_visible()
        expect(dashboard_toolbar_title).to_have_text(dashboard_toolbar_text)

        page.wait_for_timeout(5000)
