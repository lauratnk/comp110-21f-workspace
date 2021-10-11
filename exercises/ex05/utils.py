"""List utility functions part 2."""

__author__ = "730318786"

# Define your functions below


def only_evens(ls1: list[int]) -> list[int]:
    """Returns the even numbers in a list."""
    i: int = 0
    ls2: list[int] = []
    while i < len(ls1):
        if ls1[i] % 2 == 0:
            ls2.append(ls1[i])
        i += 1
    return ls2


def sub(ls1: list[int], start: int, end: int) -> list[int]:
    """Returns a the numbers in a list within the given index."""
    ls2: list[int] = []
    i: int = start
    if start == len(ls1):
        return ls2
    while i < len(ls1) and i < end:
        if i >= 0:
            ls2.append(ls1[i])
        i += 1
    return ls2


def concat(ls1: list[int], ls2: list[int]) -> list[int]:
    """Returns a list which contains all the elements of both lists."""
    i: int = 0
    ls3: list[int] = []
    while i < len(ls1):
        ls3.append(ls1[i])
        i += 1
    i2: int = 0
    while i2 < len(ls2):
        ls3.append(ls2[i2])
        i2 += 1
    return ls3
