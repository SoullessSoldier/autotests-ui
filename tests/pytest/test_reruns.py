"""Модуль автотеста."""
import random

import pytest

PLATFORM = 'Linux'


# Перезапуски реализуеются на уровне маркировки flaky
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    """Функция рандомного выбора между True и False."""
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    """Класс, использующий тестовые функции рандомного выбора."""

    def test_rerun_1(self):
        """Функция рандомного выбора между True и False."""
        assert random.choice([True, False])

    def test_rerun2(self):
        """Функция рандомного выбора между True и False."""
        assert random.choice([True, False])


# Перезапуск при выполнении условия
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == 'Windows')
def test_rerun_with_condition():
    """Функция рандомного выбора между True и False."""
    assert random.choice([True, False])
