from plates import is_valid

def main():
    test_len_char()
    test_two_letters_firts()
    test_num_in()
    test_zero()
    test_other()

# Plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_len_char():
    assert is_valid('DB') == True
    assert is_valid('ANSDFR') == True
    assert is_valid('A') == False
    assert is_valid('MDDFGTRD') == False

def test_two_letters_firts():
    assert is_valid('CC') == True
    assert is_valid('X2') == False
    assert is_valid('45') == False

def test_num_in():
    assert is_valid("XXX222") == True
    assert is_valid("XXX22A") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50I") == False

def test_other():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("Hello!") == False

if __name__ == "__main__":
    main()