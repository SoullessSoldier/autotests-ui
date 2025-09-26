"""Модуль компонента CourseViewComponent."""
import re

from components.base_component import BaseComponent

from playwright.sync_api import Page, expect


class CoursesListToolbarViewComponent(BaseComponent):
    """Класс компонента CoursesListToolbarViewComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-'
                                                        'create-course-button')

    def check_visible(self):
        """Метод для проверки видимости блока панели 'Courses'."""
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Courses')

        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        """Метод для нажатия на кнопку создания курса."""
        self.create_course_button.click()
        self.check_current_url(re.compile('.*/#/courses/create'))
