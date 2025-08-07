from playwright.sync_api import sync_playwright, expect
from time import sleep

def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_login, 
                  wait_until='networkidle' # Ждем полной загрузки страницы
                  )

        title = page.get_by_test_id('authentication-ui-course-title-text')
        expect(title).to_have_text('UI Course')

        # Выполняем JS-код для замены текста заголовка
        page.evaluate(
            '''
                const title = document.querySelector('#authentication-ui-course-title-text');
                title.textContent = 'New text'
            '''
        )
        # Добавляем паузу для наглядности
        page.wait_for_timeout(5000)

        expect(title).to_have_text('New text')

        new_text = 'New new text'
        page.evaluate(
            '''
                (text) => {
                    const title = document.querySelector('#authentication-ui-course-title-text');
                    title.textContent = text
                }
            ''',
            new_text
        )
        page.wait_for_timeout(5000)

        expect(title).to_have_text('New new text')




if __name__ == '__main__':
    test_ui()
    print("OK")