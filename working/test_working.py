from working import convert
import pytest

def main():
    test_a()
    test_t()

def test_a():
    with pytest.raises(ValueError):
        convert('7 AM - 7 PM')

def test_t():
    with pytest.raises(ValueError):
        convert('09:00 AM : 17:00')
    with pytest.raises(ValueError):
        convert('10:75 AM to 2:61 PM')
    assert convert('7 AM to 7 PM') == '07:00 to 19:00'
    assert convert('7 PM to 7 AM') == '19:00 to 07:00'

if __name__ == "__main__":
    main()