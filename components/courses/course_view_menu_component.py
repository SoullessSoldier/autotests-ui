"""Модуль компонента CourseViewMenuComponent."""
from components.base_component import BaseComponent

from elements.button import Button

from playwright.sync_api import Page


class CourseViewMenuComponent(BaseComponent):
    """Класс компонента CourseViewMenuComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.menu_button =\
            Button(page, 'course-view-menu-button', 'Menu')
        self.edit_menu_item =\
            Button(page, 'course-view-edit-menu-item', 'Edit')
        self.delete_menu_item =\
            Button(page, 'course-view-delete-menu-item', 'Delete')

    def click_edit(self, index: int):
        """
        Метод для нажатия на кнопку редактирования карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.menu_button.click(index)

        self.edit_menu_item.check_visible(index)
        self.edit_menu_item.click(index)

    def click_delete(self, index: int):
        """
        Метод для нажатия на кнопку удаления карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.menu_button.click(index)

        self.delete_menu_item.check_visible(index)
        self.delete_menu_item.click(index)
