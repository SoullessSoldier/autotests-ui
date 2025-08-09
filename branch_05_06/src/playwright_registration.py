from playwright.sync_api import sync_playwright, expect
import os

SRC_DIR = '/opt/src'

def test_ui():
    with sync_playwright() as pw:
        url_registration = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        browser = pw.chromium.launch(headless=True)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url_registration)

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path=os.path.join(SRC_DIR, "browser-state.json"))

    # Второй прогон с использованием сохраненного состояния,
    # ожидаем, что браузер попадет на внутреннюю страницу /dashboard
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state=os.path.join(SRC_DIR, "browser-state.json")) # Указываем файл с сохраненным состоянием
        page = context.new_page()

        url_dashboard = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        page.goto(url_dashboard)
        dashboard_toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_toolbar_title).to_be_visible()
        expect(dashboard_toolbar_title).to_have_text('Dashboard')

        page.wait_for_timeout(5000)


if __name__ == '__main__':
    test_ui()
    print("OK")
