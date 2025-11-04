"""Модуль настроек проекта."""
from enum import Enum
from typing import Self

from pydantic import BaseModel, DirectoryPath, EmailStr, FilePath, HttpUrl

from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    """Клас имен браузеров."""

    WEBKIT = 'webkit'
    FIREFOX = 'firefox'
    CHROMIUM = 'chromium'


class TestUser(BaseModel):
    """Класс данных тестового пользователя."""

    model_config = SettingsConfigDict(env_prefix='TEST_USER')
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    """Класс с данными пути к тестовому изображению."""

    model_config = SettingsConfigDict(env_prefix='TEST_DATA')
    image_png_file: FilePath


class Settings(BaseSettings):
    """Класс настроек проекта."""

    base_url: str = ''
    db_dsn: str = ''

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        """Инициализация настроек."""
        videos_dir = DirectoryPath('./videos')
        tracing_dir = DirectoryPath('./tracing')
        allure_results_dir = DirectoryPath('./allure-results')
        browser_state_file = FilePath('browser-state.json')

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )

    def get_base_url(self) -> str:
        """Метод возвращает значение базового url приложения (app_url)."""
        return f'{self.app_url}/'


settings = Settings.initialize()
