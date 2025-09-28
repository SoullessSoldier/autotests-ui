"""Модуль с классом страницы авторизации."""
from components.authentication.login_form_component import LoginFormComponent

from elements.button import Button
from elements.link import Link
from elements.text import Text

from pages.base_page import BasePage

from playwright.sync_api import Page


class LoginPage(BasePage):
    """Класс POM страница авторизации."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link',
                                      'Registration')
        self.wrong_email_or_password_alert =\
            Text(page, 'login-page-wrong-email-or-password-alert',
                 'Wrong email or password')

    def click_login_button(self):
        """Метод для нажатия на кнопку 'Login'."""
        self.login_button.check_visible()
        self.login_button.click()

    def click_registration_link(self):
        """Метод для нажатия на ссылку 'Registration'."""
        self.registration_link.check_visible()
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        """Метод для проверки отображения алерта с ошибкой."""
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email '
                                                           'or password')
