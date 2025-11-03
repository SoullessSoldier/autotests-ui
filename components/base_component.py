"""Модуль с базовым классом."""
from typing import Pattern

import allure

from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger('BASE_COMPONENT')


class BaseComponent:
    """Базовый класс для Page Component."""

    def __init__(self, page: Page):
        """Конструктор класса, принимающий объект Page."""
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """Метод для проверки текущего URL."""
        step = f'Check current url "{expected_url}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
