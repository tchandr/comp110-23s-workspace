"""EX05 List Utils."""


__author__ = "730564179"


def only_evens(nums: list[int]) -> list[int]:
    """Returns a list with only evens."""
    even_nums: list[int] = []
    for i in nums:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns a concat list."""
    concat_list: list[int] = []
    for i in list1:
        concat_list.append(i)
    for i in list2:
        concat_list.append(i)
    return concat_list


def sub(set: list[int], start: int, end: int) -> list[int]:
    """Returns a subset."""
    subset: list[int] = []
    if start < 0:
        start = 0
    if end > len(set):
        end = len(set)
    while start < end:
        subset.append(set[start])
        start += 1
    return subset