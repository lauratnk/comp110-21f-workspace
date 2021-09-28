"""List utility functions."""

__author__ = "730318786"


# TODO: Implement your functions here.

def all(list1: list[int], value1: int) -> bool:
    """Returns True if all numbers in list match given int, False otherwise."""
    i: int = 0
    if len(list1) == 0:
        return False
    while i < len(list1):
        if value1 != list1[i]:
            return False
        i = i + 1
    return True


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true if elements in list completely equals other list."""
    i: int = 0
    if len(list1) != len(list2):
        return False
    while i < len(list2):
        if list1[i] != list2[i]:
            return False
        i = i + 1
    return True
    

def max(list1: list[int]) -> int:
    """Returns the max int in a given list."""
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    tentative_max: int = list1[i]
    length: int = len(list1)
    while i < length:
        if list1[i] > tentative_max:
            tentative_max = list1[i]
        i = i + 1
    return tentative_max