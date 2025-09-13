import pytest


@pytest.mark.xfail(reason='Известная ошибка, исправление в следующем релизе')
def test_known_case():
    pass


@pytest.mark.xfail(reason=('Найден баг в приложении, '
                           'из-за которого тест падает с ошибкой'))
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason=('Баг уже исправили, '
                           'но на тесте все еще висит маркировка xfail'))
def test_without_bug():
    pass


@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_service_is_unavailavable():
    assert 2 == 3
