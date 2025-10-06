"""Модуль элемента ссылки Link."""
from elements.base_element import BaseElement


class Link(BaseElement):
    """Класс элемента ссылки Link."""

    @property
    def type_of(self):
        """Метод переопределяет встроенный метод из allure."""
        return 'link'

    pass
