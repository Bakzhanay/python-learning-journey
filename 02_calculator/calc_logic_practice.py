def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def divis(a, b):
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя.")
    return a / b