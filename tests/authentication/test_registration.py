"""Модуль автотеста."""
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

import pytest


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    """Класс тестов регистрации."""

    def test_successful_registration(self,
                                     registration_page: RegistrationPage,
                                     dashboard_page: DashboardPage):
        """Функция автотеста регистрации в приложении."""
        registration_page.visit('https://nikita-filonov.github.io/'
                                'qa-automation-engineer-ui-course/'
                                '#/auth/registration')

        registration_page.registration_form.fill(email='user.name@gmail.com',
                                                 username='username',
                                                 password='password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
