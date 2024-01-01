from fuel import convert,gauge
import pytest
def main():
    test_x()
    test_y()
    test_f()
    test_e()
...
def test_x():

    with pytest.raises(ValueError):
        convert("cat/dog")
    # assert convert("-1/3") == "ValueError"
    # assert convert("3/2") == "ValueError"
    assert convert("3/4") == 75 and gauge(75) == '75%'

    # assert convert('1/4') == 25 and gauge(25) == '25%'
    # assert convert('1/100') == 1 and gauge(1) == 'E'
    # assert convert('99/100') == 99 and gauge(99) == 'F'

...
def test_y():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

    # assert convert("3/0") == "ZeroDivisionError"

def test_f():
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_e():
    assert convert("1/100") == 1 and gauge(1) == 'E'

...
if __name__ == "__main__":
    main()