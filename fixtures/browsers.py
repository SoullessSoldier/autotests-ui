"""Файл фикстур."""
from collections.abc import Generator

from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage

from playwright.sync_api import Page, Playwright

import pytest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    """Сессионная фикстура для регистрации пол-ля и сохранения контекста."""
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page\
        .visit('https://nikita-filonov.github.io/qa-automation'
               '-engineer-ui-course/#/auth/registration')

    registration_page\
        .registration_form.fill(email='user.name@gmail.com',
                                username='username',
                                password='password')

    registration_page.registration_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(
        initialize_browser_state,
        playwright: Playwright,
        request: SubRequest) -> Generator[Page, None, None]:
    """Функция возвращает инстанс страницы Page с авторизованной сессией."""
    yield from initialize_playwright_page(
        playwright,
        storage_state='browser-state.json',
        test_name=request.node.name
    )


@pytest.fixture(scope='function')
def chromium_page(
        playwright: Playwright,
        request: SubRequest) -> Generator[Page, None, None]:
    """Функция возвращает инстанс страницы Page."""
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name
    )
