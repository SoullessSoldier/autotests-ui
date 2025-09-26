"""Модуль компонента ImageUploadWidgetComponent."""
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent

from playwright.sync_api import Page, expect


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
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'preview-image')

        self.image_upload_info_icon =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'info-icon')
        self.image_upload_info_title =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'info-title-text')
        self.image_upload_info_description =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'info-description-text')

        self.upload_button =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'upload-button')
        self.remove_button =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-'
                                'remove-button')
        self.upload_input =\
            page.get_by_test_id(f'{identifier}-image-upload-widget-input')

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
        expect(self.image_upload_info_icon).to_be_visible()
        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )
        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text(
            'Recommended file size 540X300'
        )
        expect(self.upload_button).to_be_visible()

        if is_image_uploaded:
            expect(self.remove_button).to_be_visible()
            expect(self.preview_image).to_be_visible()

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
