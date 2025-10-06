"""Модуль компонента ImageUploadWidgetComponent."""
import allure

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent

from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text

from playwright.sync_api import Page


class ImageUploadWidgetComponent(BaseComponent):
    """Класс компонента ImageUploadWidgetComponent."""

    def __init__(self, page: Page, identifier: str):
        """Конструктор класса.

        :param Page page: объект Page страницы из playwright
        :param str identifier: идентификатор компонента
        """
        super().__init__(page)

        self.preview_empty_view =\
            EmptyViewComponent(page, identifier)

        self.preview_image =\
            Image(page,
                  f'{identifier}-image-upload-widget-preview-image',
                  'Image')

        self.image_upload_info_icon =\
            Icon(page,
                 f'{identifier}-image-upload-widget-info-icon',
                 'Icon')
        self.image_upload_info_title =\
            Text(page,
                 f'{identifier}-image-upload-widget-info-title-text',
                 'Title')
        self.image_upload_info_description =\
            Text(page,
                 f'{identifier}-image-upload-widget-info-description-text',
                 'Description')

        self.upload_button =\
            Button(page,
                   f'{identifier}-image-upload-widget-upload-button',
                   'Upload image')
        self.remove_button =\
            Button(page,
                   f'{identifier}-image-upload-widget-remove-button',
                   'Remove image')
        self.upload_input =\
            FileInput(page,
                      f'{identifier}-image-upload-widget-input',
                      'File input')

    @allure.step('Check visible ImageUploadWidget')
    def check_visible(
            self,
            is_image_uploaded: bool = False
    ):
        """
        Метод проверяет отображение виджета.

        Проверка в зависимости от наличия загруженного изображения.

        Если is_image_uploaded = True, проверяем состояние специфичное для
        загруженной картинки.
        Если is_image_uploaded = False, проверяем наличие компонента
        *EmptyViewComponent*

        :param bool is_image_uploaded: Признак того, что картинка загружена.
        По умолчанию False.
        """
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )
        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text(
            'Recommended file size 540X300'
        )
        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        """Метод нажимает кнопку 'Remove image'."""
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        """
        Метод загружает изображение курса.

        :param str file: Путь к загружаемому изображению
        """
        self.upload_input.set_input_files(file)
