"""Модуль элемента поля загрузки файлов FileInput."""
from elements.base_element import BaseElement


class FileInput(BaseElement):
    """Класс элемента поля загрузки файлов FileInput."""

    def set_input_files(self, file: str, **kwargs):
        """
        Метод (переопределенный) для инициализации локатора.

        :param str file: Путь к загружаемому файлу
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)
