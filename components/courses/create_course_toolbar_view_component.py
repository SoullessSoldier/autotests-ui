"""Модуль компонента CreateCourseToolbarViewComponent."""
import allure

from components.base_component import BaseComponent

from elements.button import Button
from elements.text import Text

from playwright.sync_api import Page


class CreateCourseToolbarViewComponent(BaseComponent):
    """Класс компонента CreateCourseToolbarViewComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.create_course_title =\
            Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button =\
            Button(page,
                   'create-course-toolbar-create-course-button',
                   'Create course')

    @allure.step(
            'Check create course toolbar with '
            'button "create_course_disabled" '
            'state="{is_create_course_disabled}"'
    )
    def check_visible(self, is_create_course_disabled: bool = True):
        """
        Метод проверяет корректность отображения панели управления.

        :param bool is_create_course_disabled:
        Признак доступности кнопки создания курса, по умолчанию True.
        """
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

        self.create_course_button.check_visible()
        if is_create_course_disabled:
            self.create_course_button.check_disabled

        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        """Метод имитирует нажатие на кнопку создания курса."""
        self.create_course_button.click()
