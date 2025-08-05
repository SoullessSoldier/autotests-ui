from playwright.sync_api import sync_playwright, expect

def test_ui():
    with sync_playwright() as pw:
        url_registration = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
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

        dashboard_toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_toolbar_title).to_be_visible()
        expect(dashboard_toolbar_title).to_have_text('Dashboard')


if __name__ == '__main__':
    test_ui()
    print("OK")
