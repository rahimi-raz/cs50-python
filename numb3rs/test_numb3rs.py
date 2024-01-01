from numb3rs import validate
def main():
    test_a()
    test_b()

def test_a():
    assert validate("a.2.3.4") == False
    assert validate("1.w.3.4") == False
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.5.5") == False

def test_b():
    assert validate("1000.2.3.4") == False
    assert validate('255.255.255.255') == True
    assert validate('512.1.1.1') == False
    assert validate('1.512.1.1') == False
    assert validate('1.1.512.1') == False
    assert validate('1.1.1.512') == False
