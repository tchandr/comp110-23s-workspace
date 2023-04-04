"""Ex05 Test file."""


__author__ = "730564179"


from exercises.ex05.utils import only_evens, sub, concat


def test_even_usecase1() -> None:
    """Even function use case 1."""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(test) == [2, 4, 6, 8, 10]


def test_even_edge() -> None:
    """Even function edge case 1."""
    test: list[int] = []
    assert only_evens(test) == []


def test_even_usecase2() -> None:
    """Even function use case 2."""
    test: list[int] = [-5, -4, -2, 0, 2]
    assert only_evens(test) == [-4, -2, 0, 2]


def test_concat_usecase1() -> None:
    """Concat function use case 1."""
    test1: list[int] = [1, 2, 3]
    test2: list[int] = [3, 2, 1]
    assert concat(test1, test2) == [1, 2, 3, 3, 2, 1] 


def test_concat_usecase2() -> None:
    """Cpncat function use case 2."""
    test1: list[int] = [-1, -2, -3]
    test2: list[int] = [-3, -2, -1]
    assert concat(test1, test2) == [-1, -2, -3, -3, -2, -1] 


def test_concat_edge() -> None:
    """Concat function edge case 1."""
    test1: list[int] = []
    test2: list[int] = [3, 2, 1]
    assert concat(test1, test2) == [3, 2, 1]


def test_sub_usecase1() -> None:
    """Sub function use case 1."""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = 3
    end = 7
    assert sub(test, start, end) == [4, 5, 6, 7]


def test_sub_usecase2() -> None:
    """Sub function use case 2."""
    test: list[int] = [4, 4, 5, 5, 6, 6]
    start = 2
    end = 3
    assert sub(test, start, end) == [5]


def test_sub_edge() -> None:
    """Sub function edge case 1."""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = -10
    end = 11
    assert sub(test, start, end) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]