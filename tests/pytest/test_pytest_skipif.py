"""Модуль автотеста."""
import pytest
# import sys


# @pytest.mark.skipif(sys.version_info < (3, 8),
#                     reason="Требуется Python 3.8 или выше")
# def test_python_version():
#     pass

SYSTEM_VERSION = 'v1.2.0'


@pytest.mark.skipif(
    SYSTEM_VERSION == 'v1.3.0',
    reason='Тест не может быть запущен на версии системы 1.3.0'
)
def test_sytem_version_valid():
    """Тест должен выполняться только на определённой версии билда."""
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == 'v1.2.0',
    reason='Тест не может быть запущен на версии системы 1.2.0'
)
def test_sytem_version_invalid():
    """Тест должен выполняться только на определённой версии билда."""
    pass
