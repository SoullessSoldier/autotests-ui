from playwright.sync_api import sync_playwright, expect

def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_login)

        login_button = page.get_by_test_id('login-page-login-button')
        expect(login_button).to_be_disabled()
        # expect(login_button).not_to_be_disabled()



if __name__ == '__main__':
    test_ui()
    print("OK")