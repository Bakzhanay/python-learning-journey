import pytest
from calc_logic_practice import add, subtract, multi, divis

def test_add():
    assert add(45,45) == 90
    assert add(10,-20) == -10

def test_substract():
    assert subtract(75, 25) == 50
    assert subtract(2.5, 1.3) == 1.2

def test_multi():
    assert multi(5, 5) == 25
    assert multi(4, 3) == 12

def test_divis():
    assert divis(49, 7) == 7.0
    assert divis(80, 40) == 2.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divis(9, 0)