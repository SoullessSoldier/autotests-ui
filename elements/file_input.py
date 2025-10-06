"""Модуль элемента поля загрузки файлов FileInput."""
import allure

from elements.base_element import BaseElement


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
        with allure.step(
            f'Set file "{file}" to the {self.type_of} "{self.name}"'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
