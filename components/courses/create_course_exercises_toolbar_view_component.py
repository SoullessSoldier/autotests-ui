"""Модуль компонента CreateCourseExercisesToolbarViewComponent."""
from components.base_component import BaseComponent

from elements.button import Button
from elements.text import Text

from playwright.sync_api import Page


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """Класс компонента CreateCourseExercisesToolbarViewComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.exercises_title =\
            Text(page,
                 'create-course-exercises-box-toolbar-title-text',
                 'Title')
        self.create_exercise_button =\
            Button(page,
                   ('create-course-exercises-box-toolbar-'
                    'create-exercise-button'),
                   'Create exercise')

    def check_visible(self):
        """Метод проверяет корректность отображения панели управления."""
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        """Метод имитирует нажатие на кнопку создания задания."""
        self.create_exercise_button.click()
