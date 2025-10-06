"""Модуль с классом компонента SidebarListItemComponent."""
from typing import Pattern

import allure

from components.base_component import BaseComponent

from elements.button import Button
from elements.icon import Icon
from elements.text import Text

from playwright.sync_api import Page


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

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon',
                         'Icon')
        self.title =\
            Text(page, f'{identifier}-drawer-list-item-title-text',
                 'Title')
        self.button =\
            Button(page, f'{identifier}-drawer-list-item-button',
                   'Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        """Метод проверяет,что компонент отображается корректно на странице."""
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        """
        Проверка перехода на нужный раздел сайта.

        Метод выполняет клик на button и проверяет,
        что редирект произошел на нужную страницу.
        """
        self.button.click()
        self.check_current_url(expected_url)
