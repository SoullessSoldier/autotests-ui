from playwright.sync_api import sync_playwright
from time import sleep

def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_login, wait_until='networkidle')

        # Пытаемся проверить, что несуществующий локатор виден на странице
        # unknown = page.locator('#unknown')
        # expect(unknown).to_be_visible()

        # Пытаемся ввести текст в кнопку Login
        # login_button = page.get_by_test_id('login-page-login-button')
        # login_button.fill('unknown')
        
        # Пытаемся изменить текст заголовка
        page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)


if __name__ == '__main__':
    test_ui()
    print("OK")