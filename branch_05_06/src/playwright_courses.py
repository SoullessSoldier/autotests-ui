from playwright.sync_api import sync_playwright, expect
import os

SRC_DIR = '/opt/src'
STATE_PATH = os.path.join(SRC_DIR, "browser-state.json")

def test_ui():
    with sync_playwright() as pw:
        url_registration = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        browser = pw.chromium.launch(headless=True)
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

        context.storage_state(path=STATE_PATH)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STATE_PATH)
        page = context.new_page()

        url_courses = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        page.goto(url_courses)
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        no_results_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_title).to_be_visible()
        expect(no_results_title).to_have_text('There is no results')


if __name__ == '__main__':
    test_ui()
    print("OK")
