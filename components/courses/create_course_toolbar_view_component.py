"""Модуль компонента CreateCourseToolbarViewComponent."""
from components.base_component import BaseComponent, expect

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
            page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button =\
            page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        """
        Метод проверяет корректность отображения панели управления.

        :param bool is_create_course_disabled:
        Признак доступности кнопки создания курса, по умолчанию True.
        """
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

        expect(self.create_course_button).to_be_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()

        if not is_create_course_disabled:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        """Метод имитирует нажатие на кнопку создания курса."""
        self.create_course_button.click()
