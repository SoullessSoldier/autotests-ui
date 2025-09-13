"""Файл фикстуры POM LoginPage."""
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

from playwright.sync_api import Page

import pytest


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    """Фикстура инициализированной страницы LoginPage."""
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """Фикстура инициализированной страницы RegistrationPage."""
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """Фикстура инициализированной страницы DashboardPage."""
    return DashboardPage(page=chromium_page)
