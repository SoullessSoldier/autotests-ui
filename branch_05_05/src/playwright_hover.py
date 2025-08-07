from playwright.sync_api import sync_playwright

def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_login, 
                  wait_until='networkidle' # Ждем полной загрузки страницы
                  )

        registration_link = page.get_by_test_id('login-page-registration-link')
        # Выполняем наведение курсора на ссылку
        registration_link.hover()

        page.wait_for_timeout(5000)

        '''
        page.mouse.click(x, y)
        page.mouse.move(0, 100)
        page.mouse.wheel(delta_x, delta_y)
        page.mouse.up()
        '''


if __name__ == '__main__':
    test_ui()
    print("OK")