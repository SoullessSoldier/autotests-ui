"""Модуль элемента поля загрузки файлов FileInput."""
import allure

from elements.base_element import BaseElement

from tools.logger import get_logger

logger = get_logger('FILE_INPUT')


class FileInput(BaseElement):
    """Класс элемента поля загрузки файлов FileInput."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'file input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Метод (переопределенный) для инициализации локатора.

        :param str file: Путь к загружаемому файлу
        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        step = f'Set file "{file}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
