"""Модуль с базовым классом."""
from typing import Pattern

from playwright.sync_api import Page, expect


class BaseComponent:
    """Базовый класс для Page Component."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """Метод для проверки текущего URL."""
        expect(self.page).to_have_url(expected_url)
