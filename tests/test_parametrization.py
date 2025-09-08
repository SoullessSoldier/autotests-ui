"""Модуль автотеста."""
from _pytest.fixtures import SubRequest

import pytest


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest) -> str:
    """Фикстура будет возвращать три разных браузера."""
    return request.param


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    """Простой пример параметризации."""
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    """Пример параметризации с несколькими параметрами."""
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    """Пример параметризации с перемножением параметров."""
    assert len(os + browser) > 0


def test_open_browser(browser: str):
    """Пример использования параметризованной фикстуры."""
    print('Running test on browser: %s' % browser)


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    """Пример параметризации класса."""

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        """Пример метода с использованием параметров класса."""
        print('User with operations: %s' % user)

    def test_user_without_operations(self, user: str):
        """Пример метода с использованием параметров класса."""
        print('User without operations: %s' % user)


"""
@pytest.mark.parametrize(
        'phone_number',
        ['+70000000011', '+70000000022', '+70000000033'],
        ids=[
            'User with money on bank account',
            'User without money on bank account',
            'User with operations on bank account'
        ]
        )
"""
users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User with operations on bank account'
}


@pytest.mark.parametrize(
        'phone_number',
        users.keys(),
        ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
        )
def test_identifiers(phone_number: str):
    """Пример использования динамических идентификаторов."""
    pass
