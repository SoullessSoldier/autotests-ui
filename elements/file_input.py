"""Модуль элемента поля загрузки файлов FileInput."""
from elements.base_element import BaseElement


class FileInput(BaseElement):
    """Класс элемента поля загрузки файлов FileInput."""

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Метод (переопределенный) для инициализации локатора.

        :param str file: Путь к загружаемому файлу
        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)
