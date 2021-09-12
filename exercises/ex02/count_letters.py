"""Counting letters in a string."""

__author__ = "730318786"

i: int = 0
true_value: int = 0
enter_letter: str = input("What letter do you want to search for? ")
enter_word: str = str(input("Enter a word: "))
maximum: int = len(enter_word)

while i < maximum:
    if enter_letter == enter_word[i]:
        true_value = i + 1
    i = i + 1

print("Count: " + str(true_value))