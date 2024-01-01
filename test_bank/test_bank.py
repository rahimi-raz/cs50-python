from bank import value

def main():
    test_hello0()
    test_hello20()
    test_hello100()

def test_hello0():
    assert value("hello") == 0
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_hello20():
    assert value("hey") == 20
    assert value('hi there!') == 20
    assert value('How are you?') == 20

def test_hello100():
    assert value("salam") == 100
    assert value("What's up?") == 100
    assert value("good morning!") == 100

if __name__ == "__main__":
    main()