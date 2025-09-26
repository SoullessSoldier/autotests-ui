"""Модуль компонента CreateCourseExercisesToolbarViewComponent."""
from components.base_component import BaseComponent, expect

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
            page.get_by_test_id('create-course-exercises-box-toolbar-'
                                'title-text')
        self.create_exercise_button =\
            page.get_by_test_id('create-course-exercises-box-toolbar-'
                                'create-exercise-button')

    def check_visible(self):
        """Метод проверяет корректность отображения панели управления."""
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        """Метод имитирует нажатие на кнопку создания задания."""
        self.create_exercise_button.click()
