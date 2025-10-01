"""Модуль с классом компонента SidebarComponent."""
import re

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component\
    import SidebarListItemComponent

from playwright.sync_api import Page


class SidebarComponent(BaseComponent):
    """Класс боковой панели."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    def check_visible(self):
        """Метод проверяет корректное отображение компонента Sidebar."""
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    def click_logout(self):
        """
        Метод клика на Logout.

        Метод будет имитировать нажатие
        на элемент выхода из приложения (**Logout**) и проверять,
        что произошел редирект на URL **/#/auth/login**
        """
        self.logout_list_item.navigate(re.compile(r'.*/#/auth/login'))

    def click_courses(self):
        """
        Метод клика на Courses.

        Метод будет имитировать нажатие
        на элемент перехода к курсам (**Courses**) и проверять,
        что произошел редирект на URL **/#/courses**
        """
        self.logout_list_item.navigate(re.compile(r'*/#/courses'))

    def click_dashboard(self):
        """
        Метод клика на Dashboard.

        Метод будет имитировать нажатие
        на элемент перехода на панель управления (**Dashboard**) и проверять,
        что произошел редирект на URL **/#/dashboard**
        """
        self.logout_list_item.navigate(re.compile(r'*/#/dashboard'))
