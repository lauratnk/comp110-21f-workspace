"""Finding duplicate letters in a word."""

__author__ = "730318786"


def duplicates(a: str) -> str:
    """Duplicates function."""
    i_one: int = 0
    maximum: int = len(a) - 1
    while i_one < maximum:
        i_two: int = i_one + 1
        while i_two < maximum:
            if a[i_one] == a[i_two]:
                return "True"
            i_two = i_two + 1
        i_one = i_one + 1
    return "False"


enter_word: str = str(input("Enter a word: "))

final: str = duplicates(enter_word)

print("Found duplicate: " + final)