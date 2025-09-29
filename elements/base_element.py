"""Модуль базового элемента BaseElement."""

from playwright.sync_api import Locator, Page, expect


class BaseElement:
    """Класс базового элемента BaseElement."""

    def __init__(self, page: Page, locator: str, name: str):
        """
        Конструктор базового элемента BaseElement.

        :param Page page: объект Page страницы из playwright
        :param str locator:
        строка, представляющая локатор элемента (CSS-селектор, XPath и т.п.).
        :param str name: человекочитаемое имя элемента (для логов и отчетов).
        """
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Метод для инициализации локатора.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        """
        Метод для нажатия на элемент.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Метод для проверки видимости элемента на странице.

        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Метод для проверки наличия конкретного текста в элементе.

        :param str text: Текст, который нужно ввести в поле.
        :param int nth: Индекс элемента на странице, по умолчанию 0
        :param kwargs:
        Дополнительные именованные аргументы для локализации элемента.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
