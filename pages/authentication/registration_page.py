"""Модуль с классом страницы регистрации."""
import re

from components.authentication.\
    registration_form_component import RegistrationFormComponent

from elements.button import Button
from elements.link import Link

from pages.base_page import BasePage

from playwright.sync_api import Page


class RegistrationPage(BasePage):
    """Класс POM страница регистрации."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page,
                                          ('registration-page-'
                                           'registration-button'),
                                          'Registration')
        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    def click_registration_button(self):
        """Метод для нажатия на кнопку 'Registration'."""
        self.registration_button.check_visible()
        self.registration_button.click()

    def click_login_link(self):
        """Метод для нажатия на ссылку 'Registration'."""
        self.login_link.check_visible()
        self.login_link.click()
        self.check_current_url(re.compile('.*/#/auth/login'))
