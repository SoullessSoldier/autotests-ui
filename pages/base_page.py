"""Модуль с базовым классом."""
from playwright.sync_api import Page


class BasePage:
    """Базовый класс для POM."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        self.page = page

    def visit(self, url: str):
        """Метод для открытия ссылок."""
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """Метод для перезагрузки страницы."""
        self.page.reload(wait_until='domcontentloaded')
