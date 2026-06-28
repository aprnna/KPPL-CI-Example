# Import fungsi yang mau diuji dari app/main.py
from app.main import add, subtract, multiply, divide
# Import pytest untuk fitur testing (mis. pytest.raises)
import pytest


# Test case untuk fungsi add
def test_add():
    # Pastikan 2 + 3 hasilnya 5
    assert add(2, 3) == 5
    # Pastikan -1 + 1 hasilnya 0
    assert add(-1, 1) == 0


# Test case untuk fungsi subtract
def test_subtract():
    # Pastikan 10 - 4 hasilnya 6
    assert subtract(10, 4) == 6
    # Pastikan 0 - 0 hasilnya 0
    assert subtract(0, 0) == 0


# Test case untuk fungsi multiply
def test_multiply():
    # Pastikan 5 * 6 hasilnya 30
    assert multiply(5, 6) == 30
    # Pastikan -2 * 3 hasilnya -6
    assert multiply(-2, 3) == -6


# Test case untuk fungsi divide (kasus normal)
def test_divide():
    # Pastikan 20 / 4 hasilnya 5
    assert divide(20, 4) == 5
    # Pastikan 9 / 3 hasilnya 3.0 (float)
    assert divide(9, 3) == 3.0


# Test case khusus: pembagian dengan nol
def test_divide_by_zero():
    # Harapkan ValueError terlempar di blok ini
    with pytest.raises(ValueError):
        # Panggil divide(10, 0) -> seharusnya raise ValueError
        divide(10, 0)
