"""Модуль компонента RegistrationFormComponent."""
from components.base_component import BaseComponent, expect

from playwright.sync_api import Page


class RegistrationFormComponent(BaseComponent):
    """Класс компонента формы логина RegistrationFormComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-'
                                               'email-input')\
            .locator('input')
        self.username_input = page.get_by_test_id('registration-form-'
                                                  'username-input')\
            .locator('input')
        self.password_input = page.get_by_test_id('registration-form-'
                                                  'password-input')\
            .locator('input')

    def fill(self, email: str, username: str, password: str):
        """
        Метод для заполнения формы авторизации.

        :param str email: эл.адрес новой учетной записи
        :param str username: эл.адрес новой учетной записи
        :param str password: пароль новой учетной записи
        """
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

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
        expect(self.email_input).to_be_visible()
        if email is not None:
            self.email_input.fill(email)
            expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        if username is not None:
            self.username_input.fill(username)
            expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        if password is not None:
            self.password_input.fill(password)
            expect(self.password_input).to_have_value(password)
