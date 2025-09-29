"""Модуль элемента кнопки Button."""
from elements.base_element import BaseElement

from playwright.sync_api import expect


class Button(BaseElement):
    """Класс элемента кнопки Button."""

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка доступна для взаимодействия.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка недоступна для взаимодействия.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()
