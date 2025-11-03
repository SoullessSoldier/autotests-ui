"""Модуль элемента кнопки Button."""
import allure

from elements.base_element import BaseElement

from playwright.sync_api import expect

from tools.logger import get_logger

logger = get_logger('BUTTON')


class Button(BaseElement):
    """Класс элемента кнопки Button."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'button'

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка доступна для взаимодействия.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка недоступна для взаимодействия.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()
