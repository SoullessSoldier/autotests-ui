"""Модуль с классом компонента Navbar."""
from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class NavbarComponent(BaseComponent):
    """Класс для описания компонента Navbar."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.app_title =\
            page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title =\
            page.get_by_test_id('navigation-navbar-welcome-title-text')

    def check_visible(self, username: str):
        """Метод для проверки корректного отображения компонента Navbar."""
        expect(self.app_title).to_be_visible()
        expect(self.app_title).to_have_text('UI Course')

        expect(self.welcome_title).to_be_visible()
        expect(self.welcome_title).to_have_text('Welcome, %s!' % username)
