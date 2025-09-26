"""Модуль компонента CreateCourseExerciseFormComponent."""
from dataclasses import dataclass

from components.base_component import BaseComponent, expect


@dataclass
class CreateCourseExerciseParams:
    """Класс для описания параметров создания упражнения в курсе."""

    index: int
    title: str
    description: str


class CreateCourseExerciseFormComponent(BaseComponent):
    """Класс компонента CreateCourseExerciseFormComponent."""

    def click_delete_button(self, index: int):
        """
        Метод имитирует нажатие на кнопку удаления упражнения.

        :param int index - Индекс упражнения в курсе (начиная с 0)
        """
        delete_button =\
            self.page.get_by_test_id(f'create-course-exercise-{index}-'
                                     'box-toolbar-delete-exercise-button')
        delete_button.click()

    def check_visible(self, params: CreateCourseExerciseParams):
        """
        Метод для проверки видимости блока создания упражнения.

        :params CreateCourseExerciseParams params: данные в формате структуры
        датакласса *CreateCourseExerciseParams*
        """
        subtitle =\
            self.page.get_by_test_id(f'create-course-exercise-{params.index}-'
                                     'box-toolbar-subtitle-text')
        title_input =\
            self.page.get_by_test_id('create-course-exercise-form-'
                                     f'title-{params.index}-input')
        description_input =\
            self.page.get_by_test_id('create-course-exercise-form-'
                                     f'description-{params.index}-input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f'#{params.index + 1} Exercise')

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(params.title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(params.description)

    def fill(self, params: CreateCourseExerciseParams):
        """
        Метод для проверки корректности заполнения блока упражнения.

        :params CreateCourseExerciseParams params: данные в формате структуры
        датакласса *CreateCourseExerciseParams*
        """
        title_input =\
            self.page.get_by_test_id('create-course-exercise-form-'
                                     f'title-{params.index}-input')
        description_input =\
            self.page.get_by_test_id('create-course-exercise-form-'
                                     f'description-{params.index}-input')

        title_input.fill(params.title)
        expect(title_input).to_have_value(params.title)

        description_input.fill(params.description)
        expect(description_input).to_have_value(params.description)
