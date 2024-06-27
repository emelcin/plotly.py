from plotly.utils import _list_repr_elided


def test_list_repr_elided():
    result = _list_repr_elided([1, 2, 3], threshold=5)
    assert result == "[1, 2, 3]"

    result = _list_repr_elided(list(range(10)), threshold=5, edgeitems=2)
    expected = "[0, 1, ..., 8, 9]"
    assert result == expected

    result = _list_repr_elided((1, 2, 3), threshold=5)
    assert result == "(1, 2, 3)"

    result = _list_repr_elided(tuple(range(10)), threshold=5, edgeitems=2)
    expected = "(0, 1, ..., 8, 9)"
    assert result == expected

    try:
        _list_repr_elided({1, 2, 3})
    except ValueError as e:
        assert str(e) == "Invalid value of type: <class 'set'>"

