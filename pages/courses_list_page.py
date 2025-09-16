"""Модуль с классом страницы списка курсов."""
from dataclasses import dataclass

from pages.base_page import BasePage

from playwright.sync_api import Page, expect


@dataclass
class CheckVisibleCourseCardParams:
    """Класс для описания параметров карточки."""

    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CoursesListPage(BasePage):
    """Класс POM страница списка курсов."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-'
                                                 'title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-'
                                                        'create-course-button')

        # Карточка курса
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-'
                                                         'info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-'
                                                         'info-row-view-text')
        self.course_estimated_time_text =\
            page.get_by_test_id('course-estimated-time-info-row-view-text')

        # Меню курса
        self.course_menu_button =\
            page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item =\
            page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item =\
            page.get_by_test_id('course-view-delete-menu-item')

        # Пустой блок при отсутствии курсов
        self.empty_view_icon =\
            page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title =\
            page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description =\
            page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_courses_title(self):
        """Метод для проверки видимости заголовка 'Courses'."""
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        """Метод для проверки видимости пустого содержимого."""
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description)\
            .to_have_text('Results from the load test pipeline '
                          'will be displayed here')

    def check_visible_create_course_button(self):
        """Метод для проверки видимости кнопки создания курса."""
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        """Метод для нажатия на кнопку создания курса."""
        self.create_course_button.click()

    def check_visible_course_card(
            self,
            params: CheckVisibleCourseCardParams
    ):
        """
        Метод проверяет содержимое карточки курса на основе параметров.

        :param int index: Индекс карточки в списке курсов
        :param str title: Ожидаемый заголовок курса
        :param str max_score: Ожидаемый максимальный балл
        :param str min_score: Ожидаемый минимальный балл
        :param str estimated_time: Ожидаемое время прохождения
        """
        expect(self.course_image.nth(params.index)).to_be_visible()

        expect(self.course_title.nth(params.index)).to_be_visible()
        expect(self.course_title.nth(params.index))\
            .to_have_text(params.title)

        expect(self.course_max_score_text.nth(params.index))\
            .to_be_visible()
        expect(self.course_max_score_text.nth(params.index))\
            .to_have_text(f'Max score: {params.max_score}')

        expect(self.course_min_score_text.nth(params.index))\
            .to_be_visible()
        expect(self.course_min_score_text.nth(params.index))\
            .to_have_text(f'Min score: {params.min_score}')

        expect(self.course_estimated_time_text.nth(params.index))\
            .to_be_visible()
        expect(self.course_estimated_time_text.nth(params.index))\
            .to_have_text(f'Estimated time: {params.estimated_time}')

    def click_edit_course(self, index: int):
        """
        Метод для нажатия на кнопку редактирования карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_item.nth(index).click()

    def click_delete_course(self, index: int):
        """
        Метод для нажатия на кнопку удаления карточки курса.

        :param int index: Индекс карточки в списке курсов
        """
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_item.nth(index)).to_be_visible()
        self.course_delete_menu_item.nth(index).click()
