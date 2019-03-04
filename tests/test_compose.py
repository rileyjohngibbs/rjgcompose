from compose import compose


def test_compose_01(square, add_one):
    result = compose(square, add_one)(5)
    assert result == 36


def test_compose_02(triple, square, add_one):
    result = compose(triple, square, add_one)(2)
    assert result == 27
