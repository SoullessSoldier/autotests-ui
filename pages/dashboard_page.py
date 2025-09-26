"""Модуль с классом страницы дашборда."""
from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component \
    import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

from pages.base_page import BasePage

from playwright.sync_api import Page


class DashboardPage(BasePage):
    """Класс POM страницы дашборда."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)
        self.students_chart_view = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart_view =\
            ChartViewComponent(page, 'activities', 'line')
        self.courses_chart_view = ChartViewComponent(page, 'courses', 'pie')
        self.scores_chart_view = ChartViewComponent(page, 'scores', 'scatter')

    def check_visible_students_chart(self):
        """Метод для проверки видимости блока 'Students'."""
        self.students_chart_view.check_visible('Students')

    def check_visible_courses_chart(self):
        """Метод для проверки видимости блока 'Courses'."""
        self.courses_chart_view.check_visible('Courses')

    def check_visible_activities_chart(self):
        """Метод для проверки видимости блока 'Activities'."""
        self.activities_chart_view.check_visible('Activities')

    def check_visible_scores_chart(self):
        """Метод для проверки видимости блока 'Scores'."""
        self.scores_chart_view.check_visible('Scores')
