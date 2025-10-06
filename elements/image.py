"""Модуль элемента изображения Image."""
from elements.base_element import BaseElement


class Image(BaseElement):
    """Класс элемента изображения Image."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'image'

    pass
