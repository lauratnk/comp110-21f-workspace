"""First practice with dictionaries."""


__author__ = "730318786"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value types in a given dicitonary."""
    dict2 = dict()
    
    for x in dict1:
        """Iterates through each key in dict1."""
        if dict1[x] in dict2 or x in dict2:
            raise KeyError("Dictionary contains multiples of the same value.")
        else:
            dict2[dict1[x]] = x

    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns the value that appears the most frequently."""
    dict2 = dict()
    
    for x in dict1:
        """For all keys in dict1, add key name to dict2, set key name = 0."""
        dict2[x] = 0

    for x in dict1:
        """Iterate through all keys in dict1. If key of dict2 in dict1 increase the value of key in dict2 by 1."""
        if x in dict1:
            dict2[x] += 1

    finalkeys: list = []
    finalvals: list = []

    for x in dict2:
        """Separates dict2 into a list of final values and a list of final keys."""
        for x in dict2:
            finalkeys.append(x)
        for x in dict2:
            finalvals.append(dict2[x])

    return finalkeys[finalvals[(max(finalvals))]]


def count(ls1: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    dict1 = dict()
    for x in ls1:
        """Iterates through each value in the given list."""
        if x in dict1:
            """If unique value is already in dict, increase dict value by one."""
            dict1[x] += 1
        else:
            """If unique value is not already in dict, set dict value to one."""
            dict1[x] = 1

    return dict1