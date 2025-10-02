"""Модуль сценариев Allure."""
from enum import Enum


class AllureStory(str, Enum):
    """Класс сценариев Allure."""

    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    REGISTRATION = 'Registration'
    AUTHORIZATION = 'Authorization'
