"""EX07 - Dictionary Utilities."""


__author__ = "730564179"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert1() -> None:
    """Invert Test Case 1."""
    test: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    """Invert Test Case 2."""
    test: dict[str, str] = {'apple': 'cat'}
    assert invert(test) == {'cat': 'apple'}


def test_invert3() -> None:
    """Tests key value raise."""
    with pytest.raises(KeyError):
        test = {'kris': 'jordan', 'michael': 'jordan'}
        invert(test)


def test_favorite_color1() -> None:
    """Favorite Color Test Case 1."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test) == "blue"


def test_favorite_color2() -> None:
    """Favorite Color Test Case 2."""
    test: dict[str, str] = {"a": "orange", "b": "orange", "c": "orange"}
    assert favorite_color(test) == "orange"


def test_favorite_color3() -> None:
    """Favorite Color Edge Case."""
    test: dict[str, str] = {"Mark": "blue", "Jack": "yellow", "Randy": "blue", "John": "yellow"}
    assert favorite_color(test) == "blue"


def test_count1() -> None:
    """Count Test Case 1."""
    test: list[int] = ["hello", "hello", "hi", "hi", "hi", "bye"]
    assert count(test) == {"hello": 2, "hi": 3, "bye": 1}


def test_count2() -> None:
    """Count Test Case 2."""
    test: list[int] = ["a", "b", "b", "c", "c", "c", "d", "d", "d", "d"]
    assert count(test) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_count3() -> None:
    """Count Edge Case."""
    test: list[int] = []
    assert count(test) == {}