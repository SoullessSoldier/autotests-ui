"""Модуль маршрутов внутри приложения."""
from enum import Enum


class AppRoute(str, Enum):
    """Класс енумов маршрутов приложения."""

    LOGIN = './#/auth/login'
    REGISTRATION = './#/auth/registration'
    DASHBOARD = './#/dashboard'
    COURSES_CREATE = './#/courses/create'
    COURSES = './#/courses'
