import random
import string

def generate_password(length: int, use_symbols: bool = True) -> str:
    """
    Генерирует случайный пароль заданной длины.
    """
    if length <4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols

    if use_symbols:
        password_chars = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]
        # Добиваем остаток длины случайными символами из общего пула
        for _ in range(length - 4):
            password_chars.append(random.choice(all_chars))
    else:
        password_chars = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits)
        ]
        for _ in range(length - 3):
            password_chars.append(random.choice(all_chars))

    # Перемешиваем список, чтобы символы не шли по предсказуемому порядку
    random.shuffle(password_chars)

    return "". join(password_chars)
 