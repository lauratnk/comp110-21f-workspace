"""Drawing forests in a loop."""

__author__ = "730318786"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

counter: int = 1
depth: int = int(input("Depth: "))

if depth == 0:
    print()
else:
    while counter <= depth:
        print(counter * TREE)
        counter = counter + 1