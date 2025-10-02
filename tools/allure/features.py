"""Модуль функциональных блоков Allure."""
from enum import Enum


class AllureFeature(str, Enum):
    """Класс функциональных блоков Allure."""

    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    AUTHENTICATION = 'Authentication'
