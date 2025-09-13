"""Модуль с классом страницы авторизации."""
from pages.base_page import BasePage


from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    """Класс POM страница авторизации."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)
        # Локаторы элементов страницы
        self.email_input = page.get_by_test_id('login-form-email-input')\
            .locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input')\
            .locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-'
                                                     'registration-link')
        self.wrong_email_or_password_alert =\
            page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill_login_form(self, email: str, password: str):
        """Метод для заполнения формы авторизации."""
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        """Метод для нажатия на кнопку 'Login'."""
        expect(self.login_button).to_be_visible()
        self.login_button.click()

    def click_registration_link(self):
        """Метод для нажатия на ссылку 'Registration'."""
        expect(self.registration_link).to_be_visible()
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        """Метод для проверки отображения алерта с ошибкой."""
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text('Wrong email '
                                                                'or password')
