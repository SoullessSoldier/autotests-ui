"""Модуль компонента CreateCourseFormComponent."""
import allure

from components.base_component import BaseComponent

from elements.input import Input
from elements.textarea import TextArea

from playwright.sync_api import Page


class CreateCourseFormComponent(BaseComponent):
    """Класс компонента CreateCourseFormComponent."""

    def __init__(self, page: Page):
        """
        Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.create_course_title_input =\
            Input(page, 'create-course-form-title-input', 'Title')
        self.create_course_estimated_time_input =\
            Input(page,
                  'create-course-form-estimated-time-input',
                  'Estimated time')
        self.create_course_description_textarea =\
            TextArea(page,
                     'create-course-form-description-input',
                     'Description')
        self.create_course_max_score_input =\
            Input(page, 'create-course-form-max-score-input', 'Max score')
        self.create_course_min_score_input =\
            Input(page, 'create-course-form-min-score-input', 'Min score')

    @allure.step('Fill create course form')
    def fill(self,
             title: str | None,
             estimated_time: str | None,
             description: str | None,
             max_score: str | None,
             min_score: str | None
    ):
        """
        Метод заполняет форму создания курса.

        :param str | None title: Ожидаемый заголовок курса
        :param str | None estimated_time: Ожидаемое время прохождения
        :param str | None description: Ожидаемое описание курса
        :param str | None max_score: Ожидаемый максимальный балл
        :param str | None min_score: Ожидаемый минимальный балл
        """
        self.create_course_title_input.fill(title)
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_estimated_time_input\
            .check_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea\
            .check_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input\
            .check_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input\
            .check_have_value(min_score)

    @allure.step('Check visible create course')
    def check_visible(self,
                      title: str | None,
                      estimated_time: str | None,
                      description: str | None,
                      max_score: str | None,
                      min_score: str | None):
        """
        Метод проверяет наличие полей формы и их значения.

        :param str | None title: Ожидаемый заголовок курса
        :param str | None estimated_time: Ожидаемое время прохождения
        :param str | None description: Ожидаемое описание курса
        :param str | None max_score: Ожидаемый максимальный балл
        :param str | None min_score: Ожидаемый минимальный балл
        """
        self.create_course_title_input.check_visible()
        if title is not None:
            self.create_course_title_input.fill(title)
            self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        if estimated_time is not None:
            self.create_course_estimated_time_input.fill(estimated_time)
            self.create_course_estimated_time_input\
                .check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        if description is not None:
            self.create_course_description_textarea.fill(description)
            self.create_course_description_textarea\
                .check_have_value(description)

        self.create_course_max_score_input.check_visible()
        if max_score is not None:
            self.create_course_max_score_input.fill(max_score)
            self.create_course_max_score_input\
                .check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        if min_score is not None:
            self.create_course_min_score_input.fill(min_score)
            self.create_course_min_score_input\
                .check_have_value(min_score)
