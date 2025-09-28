"""Модуль элемента кнопки Button."""
from elements.base_element import BaseElement

from playwright.sync_api import expect


class Button(BaseElement):
    """Класс элемента кнопки Button."""

    def check_enabled(self, **kwargs):
        """Метод проверяет, что кнопка доступна для взаимодействия."""
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        """Метод проверяет, что кнопка недоступна для взаимодействия."""
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()
