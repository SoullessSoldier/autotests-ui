"""Модуль с классом страницы создания курса."""
from components.courses.create_course_exercise_form_component \
    import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component \
    import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component \
    import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component \
    import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component \
    import ImageUploadWidgetComponent


from pages.base_page import BasePage

from playwright.sync_api import Page


class CreateCoursePage(BasePage):
    """Класс POM страница создания курса."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.create_course_form = CreateCourseFormComponent(page)

        self.image_upload_widget =\
            ImageUploadWidgetComponent(page, 'create-course-preview')

        self.exercises_empty_view =\
            EmptyViewComponent(page, 'create-course-exercises')

        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)

        self.create_exercises_toolbar =\
            CreateCourseExercisesToolbarViewComponent(page)
