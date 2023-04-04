"""List Utility Functions."""


__author__ = "730564179"


def all(input: list[int], number: int) -> bool:
    """Checks if list contains the same integer value."""
    idx: int = 0
    if input == []:
        return False
    while True and idx < len(input):
        if number != input[idx]:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Returns max value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    idx: int = 0
    max: int = input[0]
    while idx < len(input):
        if max < input[idx]:
            max = input[idx]
        idx += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two lists are equal."""
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True