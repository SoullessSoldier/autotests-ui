"""Модуль с классом компонента ChartViewComponent."""
import allure

from components.base_component import BaseComponent

from elements.image import Image
from elements.text import Text

from playwright.sync_api import Page


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
            Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart =\
            Image(page, f'{identifier}-{chart_type}-chart', 'Image')

    @allure.step('Check visible chart view "{title}"')
    def check_visible(self, title: str):
        """Метод проверяет,что компонент отображается корректно на странице."""
        self.title.check_visible()
        self.title.check_have_text(title)
        self.chart.check_visible()
