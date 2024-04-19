from app import add, sub


def test_add_two_positive():
    a = 2
    b = 3
    result = add(a, b)
    assert result == 5


def test_sub_two_positive():
    a = 2
    b = 3
    result = sub(a, b)
    assert result == -1
