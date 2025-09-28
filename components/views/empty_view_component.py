"""Модуль компонента EmptyViewComponent."""
from components.base_component import BaseComponent

from elements.icon import Icon
from elements.text import Text

from playwright.sync_api import Page


class EmptyViewComponent(BaseComponent):
    """Класс компонента EmptyViewComponent."""

    def __init__(self, page: Page, identifier: str):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        :param str identifier: идентификатор компонента
        """
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon',
                         'Icon')
        self.title = Text(page, f'{identifier}-empty-view-title-text',
                          'Title')
        self.description =\
            Text(page, f'{identifier}-empty-view-description-text',
                 'Description')

    def check_visible(self, title: str, description: str):
        """
        Метод проверяет,что компонент отображается корректно на странице.

        :param str title: текст заголовка компонента
        :param str description: текст описания компонента
        """
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
