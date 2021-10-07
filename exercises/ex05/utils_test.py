"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730318786"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens1() -> None:
    """Test only_evens."""
    a: list[int] = [1, 5, 9]
    assert only_evens(a) == []


def test_only_evens2() -> None:
    """Test only_evens."""
    a: list[int] = []
    assert only_evens(a) == [] 


def test_only_evens3() -> None:
    """Test only_evens."""
    a: list[int] = [4, 6, 2]
    assert only_evens(a) == [4, 6, 2]


def test_sub1() -> None:
    """Test sub."""
    a: list[int] = [0, 1, 3, 3, 5]
    assert sub(a, 2, 4) == [3, 3]


def test_sub2() -> None:
    """Test sub."""
    a: list[int] = [0, 1, 3, 3, 5]
    assert sub(a, -2, 2) == [0, 1]


def test_sub3() -> None:
    """Test sub."""
    a: list[int] = [0, 1, 3, 3, 5]
    assert sub(a, 5, 7) == []


def test_concat1() -> None:
    """Test concat."""
    a: list[int] = []
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3]


def test_concat2() -> None:
    """Test concat."""
    a: list[int] = [0]
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [0, 1, 2, 3] 


def test_concat3() -> None:
    """Test concat."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []