"""Модуль с классом компонента ChartViewComponent."""
from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class ChartViewComponent(BaseComponent):
    """Класс компонента ChartViewComponent."""

    def __init__(self, page: Page, identifier: str, chart_type: str):
        """
        Конструктор класса.

        Принимает объект Page и идентификатор компонента.

        :param Page page: объект Page страницы из playwright
        :param str identifier: идентификатор компонента
        (students, activities, courses, scores)
        :param str chart_type: тип диаграммы (bar, line, pie, scatter)
        """
        super().__init__(page)

        self.title =\
            page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart =\
            page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        """Метод проверяет,что компонент отображается корректно на странице."""
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.chart).to_be_visible()
