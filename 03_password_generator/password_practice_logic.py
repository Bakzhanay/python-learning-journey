import random
import string

def generate_password(length: int, use_symbols: bool=True) -> str:
    if length < 4:
        raise ValueError("Пароль не может состоять меньше чем из 4-х символов.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    all_сhars = lower + upper + digits + symbols

    if use_symbols:
        password_chars = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]
        for _ in range(length-4):
            password_chars.append(random.choice(all_сhars))
            
    else:
        password_chars = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits)
        ]
        for _ in range(length-3):
            password_chars.append(random.choice(all_сhars))

    random.shuffle(password_chars)

    return "".join(password_chars)
