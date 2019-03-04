from compose import compose


def test_compose_01(square, add_one):
    result = compose(square, add_one)(5)
    assert result == 36
