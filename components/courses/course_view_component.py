"""Модуль компонента CourseViewComponent."""
from components.base_component import BaseComponent
from components.courses.\
    course_view_menu_component import CourseViewMenuComponent

from elements.image import Image
from elements.text import Text

from playwright.sync_api import Page


class CourseViewComponent(BaseComponent):
    """Класс компонента CourseViewComponent."""

    def __init__(self, page: Page):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        """
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'Preview')
        self.max_score_text =\
            Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text =\
            Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text =\
            Text(page,
                 'course-estimated-time-info-row-view-text',
                 'Estimated time')

    def check_visible(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
            ):
        """
        Метод для проверки видимости блока карточки курса.

        :param int index: Индекс карточки в списке курсов (начиная с 0)
        :param str title: Ожидаемый заголовок курса
        :param str max_score: Ожидаемая максимальная оценка на курсе
        :param str min_score: Ожидаемая минимальная оценка на курсе
        :param str estimated_time: Ожидаемая время прохождения курса
        """
        self.image.check_visible(index)

        self.title.check_visible(index)
        self.title.check_have_text(title, index)

        self.max_score_text.check_visible(index)
        self.max_score_text\
            .check_have_text(f'Max score: {max_score}', nth=index)

        self.min_score_text.check_visible(index)
        self.min_score_text\
            .check_have_text(f'Min score: {min_score}', nth=index)

        self.estimated_time_text.check_visible(index)
        self.estimated_time_text\
            .check_have_text(f'Estimated time: {estimated_time}', nth=index)
