"""Модуль экспериментов с pydantic."""
from pydantic import BaseModel


class User(BaseModel):
    """Класс пользователя."""

    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    'id': 1,
    'username': 'John Doe',
    'email': 'john@example.com'
}

user = User(**user_data)
print(user)
print(user.is_active)

invalid_user_data = {
    'id': 'first',
    'username': 'John_doe',
    'email': 'johan@example.com'
}

try:
    invalid_user = User(**invalid_user_data)
except Exception as e:
    print('Validation error', e)
