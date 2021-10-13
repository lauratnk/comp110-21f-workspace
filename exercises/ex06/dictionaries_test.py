"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730318786"


def test_invert1() -> None:
    """Test invert."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    """Test invert."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert3() -> None:
    """Test invert."""
    a: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(a) == KeyError


def test_favorite_color1() -> None:
    """Green favorite."""
    a: dict[str, str] = {'laura': 'green', 'kayla': 'blue', 'simone': 'green', 'sophie': 'purple'}
    assert favorite_color(a) == 'green'


def test_favorite_color2() -> None:
    """Same favorite."""
    a: dict[str, str] = {'laura': 'green', 'kayla': 'green', 'simone': 'green', 'sophie': 'green'}
    assert favorite_color(a) == 'green'


def test_favorite_color3() -> None:
    """Tie for favorite."""
    a: dict[str, str] = {'laura': 'blue', 'kayla': 'blue', 'simone': 'green', 'sophie': 'green'}
    assert favorite_color(a) == 'blue'


def test_count1() -> None:
    """Test count."""
    a: list[str] = ['cat', 'dog', 'mouse', 'dog', 'dog', 'cat']
    assert count(a) == {'cat': 2, 'dog': 3, 'mouse': 1}


def test_count2() -> None:
    """Test count."""
    a = []
    assert count(a) == {}


def test_count3() -> None:
    """Test count."""
    a = ['cat', 'cat', 'cat']
    assert count(a) == {'cat': 3}