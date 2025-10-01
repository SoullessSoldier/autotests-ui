"""Модуль с классом страницы списка курсов."""
from dataclasses import dataclass

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component\
    import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent

from pages.base_page import BasePage

from playwright.sync_api import Page, expect


@dataclass
class CheckVisibleCourseCardParams:
    """Класс для описания параметров карточки."""

    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CoursesListPage(BasePage):
    """Класс POM страница списка курсов."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def click_edit_course(self, index: int):
        """
        Метод для нажатия на кнопку редактирования карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.course_view.menu.menu_button.click(index)

        self.course_view.menu.edit_menu_item.check_visible(index)
        self.course_view.menu.edit_menu_item.click(index)

    def click_delete_course(self, index: int):
        """
        Метод для нажатия на кнопку удаления карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_item.nth(index)).to_be_visible()
        self.course_delete_menu_item.nth(index).click()
