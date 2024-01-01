from twttr import shorten
def main():
    test_lettercases()
    test_numb()
    test_punc()

def test_lettercases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwITtEer') == 'TwTtr'

def test_numb():
    assert shorten('1234') == '1234'

def test_punc():
    assert shorten('!?') == '!?'

if __name__ == "__main__":
    main()
