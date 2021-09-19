"""An example of a function definition."""

def my_max(a: int, b: int) -> int:
    """Returns largest argument."""
    if a >= b: 
        return a
    else:
        return b


x: int = 27
y: int = 5 + 2
z: int = my_max(x, y)

print(z)
