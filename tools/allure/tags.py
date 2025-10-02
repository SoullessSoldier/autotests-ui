"""Модуль тегов."""
from enum import Enum


class AllureTag(str, Enum):
    """Модуль тегов для Allure."""

    COURSES = 'COURSES'
    DASHBOARD = 'DASHBOARD'
    REGRESSION = 'REGRESSION'
    USER_LOGIN = 'USER_LOGIN'
    NAVIGATION = 'NAVIGATION'
    REGISTRATION = 'REGISTRATION'
    AUTHORIZATION = 'AUTHORIZATION'
