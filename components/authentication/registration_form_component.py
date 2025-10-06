"""Модуль компонента RegistrationFormComponent."""
import allure

from components.base_component import BaseComponent

from elements.input import Input

from playwright.sync_api import Page


class RegistrationFormComponent(BaseComponent):
    """Класс компонента формы логина RegistrationFormComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input',
                                 'Email')
        self.username_input = Input(page, 'registration-form-username-input',
                                    'Username')
        self.password_input = Input(page, 'registration-form-password-input',
                                    'Password')

    @allure.step('Fill registration form with parameters: '
                 '"email"={email}, "username"={username}, '
                 '"password"={password}')
    def fill(self, email: str, username: str, password: str):
        """
        Метод для заполнения формы авторизации.

        :param str email: эл.адрес новой учетной записи
        :param str username: эл.адрес новой учетной записи
        :param str password: пароль новой учетной записи
        """
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step('Check visible registration form')
    def check_visible(self,
                      email: str | None = None,
                      username: str | None = None,
                      password: str | None = None):
        """
        Метод для проверки (или проверки заполненной) формы регистрации.

        :param str | None email: эл.адрес новой учетной записи (опционально)
        :param str | None username: эл.адрес новой учетной записи (опционально)
        :param str | None password: пароль новой учетной записи (опционально)
        """
        self.email_input.check_visible()
        if email is not None:
            self.email_input.fill(email)
            self.email_input.check_have_value(email)

        self.username_input.check_visible()
        if username is not None:
            self.username_input.fill(username)
            self.username_input.check_have_value(username)

        self.password_input.check_visible()
        if password is not None:
            self.password_input.fill(password)
            self.password_input.check_have_value(password)
