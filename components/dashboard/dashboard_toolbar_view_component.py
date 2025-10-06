"""Модуль компонента DashboardToolbarViewComponent."""
import allure

from components.base_component import BaseComponent

from elements.text import Text

from playwright.sync_api import Page


class DashboardToolbarViewComponent(BaseComponent):
    """Класс компонента DashboardToolbarViewComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.dashboard_title = \
            Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check visible dashboard toolbar')
    def check_visible(self):
        """Метод проверяет корректность отображения панели управления."""
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')
