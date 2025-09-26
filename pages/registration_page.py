"""Модуль с классом страницы регистрации."""
from components.authentication.\
    registration_form_component import RegistrationFormComponent

from pages.base_page import BasePage


from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    """Класс POM страница регистрации."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-'
                                                       'registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def click_registration_button(self):
        """Метод для нажатия на кнопку 'Registration'."""
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()

    def click_login_link(self):
        """Метод для нажатия на ссылку 'Registration'."""
        expect(self.login_link).to_be_visible()
        self.login_link.click()
