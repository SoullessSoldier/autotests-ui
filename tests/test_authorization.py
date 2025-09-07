"""Модуль автотеста."""
from playwright.sync_api import expect, sync_playwright


def test_wrong_email_or_password_authorization():
    """Функция автотеста авторизации в приложении."""
    with sync_playwright() as playwright:
        url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui'
               '-course/#/auth/login')
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        email_input_id = 'login-form-email-input'
        email_value = 'user.name@gmail.com'
        email_input = page.get_by_test_id(email_input_id).locator('input')
        email_input.fill(email_value)

        password_input_id = 'login-form-password-input'
        password_value = 'password'
        password_input = page.get_by_test_id(password_input_id
                                             ).locator('input')
        password_input.fill(password_value)

        login_button_id = 'login-page-login-button'
        login_button = page.get_by_test_id(login_button_id)
        login_button.click()

        user_alert_id = 'login-page-wrong-email-or-password-alert'
        user_alert_text = 'Wrong email or password'
        wrong_email_or_password_alert = page.get_by_test_id(user_alert_id)
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text(user_alert_text)
