"""Модуль компонента CourseViewComponent."""
import re

import allure

from components.base_component import BaseComponent

from elements.button import Button
from elements.text import Text

from playwright.sync_api import Page


class CoursesListToolbarViewComponent(BaseComponent):
    """Класс компонента CoursesListToolbarViewComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button =\
            Button(page,
                   'courses-list-toolbar-create-course-button',
                   'Create course')

    @allure.step('Check visible courses list toolbar')
    def check_visible(self):
        """Метод для проверки видимости блока панели 'Courses'."""
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        """Метод для нажатия на кнопку создания курса."""
        self.create_course_button.click()
        self.check_current_url(re.compile('.*/#/courses/create'))
