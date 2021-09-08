"""Counting letters in a string."""

__author__ = "730318786"

i: int = 0
enter_letter: str = input("What letter do you want to search for? ")
enter_word: str = str(input("Enter a word: "))
maximum: int = len(enter_word)

""" uhhhhhh v 4 """
if i >= maximum:
    i = 0
else:
    while enter_word[i] != enter_letter:
        i = i + 1
print(str(i + 1))