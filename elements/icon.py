"""Модуль элемента иконки Icon."""
from elements.base_element import BaseElement


class Icon(BaseElement):
    """Класс элемента иконки Icon."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'icon'

    pass
