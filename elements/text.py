"""Модуль элемента блока с текстом Text."""
from elements.base_element import BaseElement


class Text(BaseElement):
    """Класс элемента блока с текстом Text."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'text'

    pass
