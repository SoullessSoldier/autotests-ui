from playwright.sync_api import sync_playwright
from time import sleep

def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_login)

        # Устанавливаем фокус на поле Email
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.focus()

        # Посимвольно имитируем нажатия клавиш для ввода текста
        for character in 'user@gmail.com':
            # Добавляем задержку 300 мс для имитации реального ввода
            page.keyboard.press(character, delay=300)

        # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
        page.keyboard.press('ControlOrMeta+A')

        # Ждём 5 секунд для наглядности результата
        page.wait_for_timeout(5000)


if __name__ == '__main__':
    test_ui()
    print("OK")