from example import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 1) == 1