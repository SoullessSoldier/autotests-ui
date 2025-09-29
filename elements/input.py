"""Модуль элемента поля ввода Input."""
from typing import override

from elements.base_element import BaseElement

from playwright.sync_api import Locator, expect


class Input(BaseElement):
    """Класс элемента поля ввода Input."""

    @override
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Метод (переопределенный) для инициализации локатора.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        """
        Метод, который заполняет поле ввода указанным текстом.

        :param str value: Текст, который нужно ввести в поле.
        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: str = 0, **kwargs):
        """
        Метод, который проверяет значение, находящееся в поле ввода.

        :param str value: Текст, который ожидается в поле.
        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
