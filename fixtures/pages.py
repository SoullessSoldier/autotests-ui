"""Файл фикстуры POM LoginPage."""
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage

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


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    """Фикстура инициализированной страницы DashboardPage с состоянием."""
    return DashboardPage(page=chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    """Фикстура инициализированной страницы CoursesListPage."""
    return CoursesListPage(page=chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    """Фикстура инициализированной страницы CreateCoursePage."""
    return CreateCoursePage(page=chromium_page_with_state)
