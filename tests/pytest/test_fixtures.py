"""Модуль автотеста."""
import pytest


# Фикстура, которая будет автоматически вызываться для каждого теста
@pytest.fixture(autouse=True)
def send_analytics_data():
    """Функция отправки данных при каждом тесте."""
    print('[AUTOUSE] Отправляем данные в сервис аналитики')


# Фикстура для инициализации настроек автотестов на уровне сессии
@pytest.fixture(scope='session')
def settings():
    """Функция инициализации настроек один раз на всю сессию тестов."""
    print('[SESSION] Инициализируем настройки автотестов')


# Фикстура для создания данных пользователя, которая будет выполняться
# один раз на класс тестов
@pytest.fixture(scope='class')
def user():
    """Функция создает тестовые данные для класса тестов."""
    print('[CLASS] Создаем данные пользователя один раз на тестовый класс')


# Фикстура для открытия браузера, выполняющаяся для каждого теста
@pytest.fixture(scope='function')
def browser():
    """Функция открытия браузера на каждый автотест."""
    print('[FUNCTION] Открываем браузер на каждый автотест')


class TestUserFlow:
    """Тестовый класс действий пользователя."""

    def test_user_can_login(self, settings, user, browser):
        """Тестовая функция."""
        pass

    def test_user_can_create_course(self, settings, user, browser):
        """Тестовая функция."""
        pass


class TestAccountFlow:
    """Тестовый класс действий с учетной записью пользователя."""

    def test_user_account(self, settings, user, browser):
        """Тестовая функция."""
        pass
