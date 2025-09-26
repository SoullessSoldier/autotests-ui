"""Модуль компонента DashboardToolbarViewComponent."""
from components.base_component import BaseComponent, expect

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
            page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self):
        """Метод проверяет корректность отображения панели управления."""
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')
