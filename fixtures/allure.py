"""Файл фикстур для allure environment."""
import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    """Функция сохранения allure environment в файл."""
    yield
    create_allure_environment_file()
