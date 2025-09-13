"""Модуль с классом страницы дашборда."""
from pages.base_page import BasePage

from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    """Класс POM страница дашборда."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)
        # Локаторы элементов страницы
        self.dashboard_title = \
            page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_title_text(self):
        """Метод для проверки видимости заголовка 'Dashboard'."""
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')
