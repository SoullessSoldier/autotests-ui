"""Модуль компонента LoginFormComponent."""
from components.base_component import BaseComponent

from elements.input import Input

from playwright.sync_api import Page


class LoginFormComponent(BaseComponent):
    """Класс компонента формы логина LoginFormComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input =\
            Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        """
        Метод для заполнения формы авторизации.

        :param str email: эл.адрес зарегистрированной учетной записи
        :param str password: пароль зарегистрированной учетной записи
        """
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def check_visible(self,
                      email: str | None = None,
                      password: str | None = None
                      ):
        """
        Метод для проверки (или проверки заполненной) формы авторизации.

        :param str | None email:
        эл.адрес зарегистрированной учетной записи (опционально)
        :param str | None password:
        пароль зарегистрированной учетной записи (опционально)
        """
        self.email_input.check_visible()
        if email is not None:
            self.email_input.fill(email)
            self.email_input.check_have_value(email)

        self.password_input.check_visible()
        if password is not None:
            self.password_input.fill(password)
            self.password_input.check_have_value(password)
