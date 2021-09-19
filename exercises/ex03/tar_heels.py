"""An exercise in remainders and boolean logic."""

__author__ = "730318786"


# Begin your solution here...
def tarheels(a: int) -> str:
    """Tarheel parameters."""
    if a % 2 == 0 or a % 7 == 0:
        if a % 2 == 0 and a % 7 == 0:
            return "TAR HEELS"
        if a % 2 == 0:
            return "TAR"
        if a % 7 == 0:
            return "HEELS"
    else:
        return "CAROLINA"

enter_number: int = int(input("Enter an int: "))

final: str = tarheels(enter_number)

print(final)