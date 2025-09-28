"""Модуль компонента CreateCourseExerciseFormComponent."""
from dataclasses import dataclass

from components.base_component import BaseComponent

from elements.button import Button
from elements.input import Input
from elements.text import Text

from playwright.sync_api import Page


@dataclass
class CreateCourseExerciseParams:
    """Класс для описания параметров создания упражнения в курсе."""

    index: int
    title: str
    description: str


class CreateCourseExerciseFormComponent(BaseComponent):
    """Класс компонента CreateCourseExerciseFormComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса компонента CreateCourseExerciseFormComponent.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.delete_exercise_button = Button(
            page,
            ('create-course-exercise-{index}-'
             'box-toolbar-delete-exercise-button'),
            'Delete exercise'
        )
        self.subtitle = Text(
            page,
            'create-course-exercise-{index}-box-toolbar-subtitle-text',
            'Exercise subtitle'
        )
        self.title_input = Input(
            page,
            'create-course-exercise-form-title-{index}-input',
            'Title'
        )
        self.description_input = Input(
            page,
            'create-course-exercise-form-description-{index}-input',
            'Description'
        )

    def click_delete_button(self, index: int):
        """
        Метод имитирует нажатие на кнопку удаления упражнения.

        :param int index - Индекс упражнения в курсе (начиная с 0)
        """
        self.delete_exercise_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str):
        """
        Метод для проверки видимости блока создания упражнения.

        :param int index - Индекс упражнения в курсе (начиная с 0)
        :param str title - Название упражнения
        :param str description - Описание упражнения
        """
        self.subtitle.check_visible()
        self.subtitle.check_have_text(f'#{index + 1} Exercise', index=index)

        self.title_input.check_visible()
        self.title_input.check_have_value(title, index=index)

        self.description_input.check_visible()
        self.description_input.check_have_value(description, index=index)

    def fill(self, index: int, title: str, description: str):
        """
        Метод для проверки корректности заполнения блока упражнения.

        :param int index - Индекс упражнения в курсе (начиная с 0)
        :param str title - Название упражнения
        :param str description - Описание упражнения
        """
        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description, index=index)
