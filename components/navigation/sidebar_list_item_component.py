"""Модуль с классом компонента SidebarListItemComponent."""
from typing import Pattern

from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class SidebarListItemComponent(BaseComponent):
    """Класс компонента SidebarListItemComponent."""

    def __init__(self, page: Page, identifier: str):
        """
        Конструктор класса.

        Принимает объект Page и идентификатор компонента.

        :param Page page: объект Page страницы из playwright
        :param str identifier: идентификатор компонента
        """
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title =\
            page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button =\
            page.get_by_test_id(f'{identifier}-'
                                'drawer-list-item-button')

    def check_visible(self, title: str):
        """Метод проверяет,что компонент отображается корректно на странице."""
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        """
        Проверка перехода на нужный раздел сайта.

        Метод выполняет клик на button и проверяет,
        что редирект произошел на нужную страницу.
        """
        self.button.click()
        self.check_current_url(expected_url)
