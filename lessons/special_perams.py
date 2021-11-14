"""LS26."""

from typing import Union

# When in type = "_" form, the peram is optional. Optional perams cannot come before not optional ones.


def hello(name: Union[str, int, float] = "World") -> str:
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return "Hello alien from sector " + str(name)
    else:
        return result + str(name)


# Example from Gradescope
def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result


print(add(110.0, "110.0"))
# Calling hello with no argument leads to use of default value.
print(hello())
# Calling hello with one argument overrides the default value
print(hello("Laura"))
print(hello(110))
print(hello(3.14))