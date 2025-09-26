"""Модуль компонента CreateCourseFormComponent."""
from components.base_component import BaseComponent, expect

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
            page.get_by_test_id('create-course-form-title-input')\
                .locator('input')
        self.create_course_estimated_time_input =\
            page.get_by_test_id('create-course-form-estimated-time-input')\
                .locator('input')
        self.create_course_description_textarea =\
            page.get_by_test_id('create-course-form-description-input')\
                .locator('textarea').first
        self.create_course_max_score_input =\
            page.get_by_test_id('create-course-form-max-score-input')\
                .locator('input')
        self.create_course_min_score_input =\
            page.get_by_test_id('create-course-form-min-score-input')\
                .locator('input')

    def fill(self, title, estimated_time, description, max_score, min_score):
        """
        Метод заполняет форму создания курса.

        :param str title: Ожидаемый заголовок курса
        :param str estimated_time: Ожидаемое время прохождения
        :param str description: Ожидаемое описание курса
        :param str max_score: Ожидаемый максимальный балл
        :param str min_score: Ожидаемый минимальный балл
        """
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        expect(self.create_course_estimated_time_input)\
            .to_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        expect(self.create_course_description_textarea)\
            .to_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input)\
            .to_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input)\
            .to_have_value(min_score)

    def check_visible(self,
                      title,
                      estimated_time,
                      description,
                      max_score,
                      min_score):
        """
        Метод проверяет наличие полей формы и их значения.

        :param str title: Ожидаемый заголовок курса
        :param str estimated_time: Ожидаемое время прохождения
        :param str description: Ожидаемое описание курса
        :param str max_score: Ожидаемый максимальный балл
        :param str min_score: Ожидаемый минимальный балл
        """
        expect(self.create_course_title_input).to_be_visible()
        if title:
            self.create_course_title_input.fill(title)
            expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        if estimated_time:
            self.create_course_estimated_time_input.fill(estimated_time)
            expect(self.create_course_estimated_time_input)\
                .to_have_value(estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        if description:
            self.create_course_description_textarea.fill(description)
            expect(self.create_course_description_textarea)\
                .to_have_value(description)

        expect(self.create_course_max_score_input).to_be_visible()
        if max_score:
            self.create_course_max_score_input.fill(max_score)
            expect(self.create_course_max_score_input)\
                .to_have_value(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        if min_score:
            self.create_course_min_score_input.fill(min_score)
            expect(self.create_course_min_score_input)\
                .to_have_value(min_score)
