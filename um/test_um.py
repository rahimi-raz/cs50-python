from um import count
import pytest

def main():
    test_t()


def test_t():
    assert count('um? umm um! uumm') == 2
    assert count('test') == 0
    assert count('Um') == 1
    assert count("Um... test") == 1
    assert count("Um, thanks, um, test") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

if __name__ == "__main__":
    main()