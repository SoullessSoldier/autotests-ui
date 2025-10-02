"""Модуль эпиков Allure."""
from enum import Enum


class AllureEpic(str, Enum):
    """Класс перечисления эпиков Allure."""

    LMS = 'LMS System'
    STUDENT = 'Student system'
    ADMINISTRATION = 'Administration system'
