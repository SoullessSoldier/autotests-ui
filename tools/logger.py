"""Модуль логирования."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Функция настройки логгера."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
