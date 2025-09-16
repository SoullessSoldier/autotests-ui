"""Модуль автотеста."""
import pytest


@pytest.mark.xfail(reason='Известная ошибка, исправление в следующем релизе')
def test_known_case():
    """Тест ожидаемо провалится, исправление в следующем релизе."""
    pass


@pytest.mark.xfail(reason=('Найден баг в приложении, '
                           'из-за которого тест падает с ошибкой'))
def test_with_bug():
    """Тест ожидаемо провалится из-за известной ошибки в коде."""
    assert 1 == 2


@pytest.mark.xfail(reason=('Баг уже исправили, '
                           'но на тесте все еще висит маркировка xfail'))
def test_without_bug():
    """С теста не сняли маркировку."""
    pass


@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_service_is_unavailavable():
    """Тест зависит от внешнего сервиса."""
    assert 2 == 3
