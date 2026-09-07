from password_logic import generate_password
import pytest
import string

def test_password_success():
    password = generate_password(8)
    assert len(password) == 8
    assert isinstance(password, str)

def test_password():
    with pytest.raises(ValueError):
        generate_password(3)

def test_password_without_symbols():
    password = generate_password(10, use_symbols=False)
    assert len(password) == 10
    # Проверяем, что ни один символ из пунктуации не содержится в пароле
    for char in string.punctuation:
        assert char not in password