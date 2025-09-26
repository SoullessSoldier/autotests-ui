"""Модуль компонента EmptyViewComponent."""
from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class EmptyViewComponent(BaseComponent):
    """Класс компонента EmptyViewComponent."""

    def __init__(self, page: Page, identifier: str):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        :param str identifier: идентификатор компонента
        """
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description =\
            page.get_by_test_id(f'{identifier}-empty-view-description-text')

    def check_visible(self, title: str, description: str):
        """
        Метод проверяет,что компонент отображается корректно на странице.

        :param str title: текст заголовка компонента
        :param str description: текст описания компонента
        """
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)
