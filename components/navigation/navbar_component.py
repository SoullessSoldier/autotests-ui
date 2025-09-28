"""Модуль с классом компонента Navbar."""
from components.base_component import BaseComponent

from elements.text import Text

from playwright.sync_api import Page


class NavbarComponent(BaseComponent):
    """Класс для описания компонента Navbar."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.app_title =\
            Text(page, 'navigation-navbar-app-title-text', 'App title')
        self.welcome_title =\
            Text(page, 'navigation-navbar-welcome-title-text', 'Welcome Title')

    def check_visible(self, username: str):
        """Метод для проверки корректного отображения компонента Navbar."""
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text('Welcome, %s!' % username)
