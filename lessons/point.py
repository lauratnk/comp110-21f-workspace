"""Exmaple of a point class."""


class Point:
    x: float
    y: float
    

    def __init__(self, x: float, y: float):
        """Initialize a POoint with its x and y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates components by a factor."""
        self.x *= factor
        self.y *= factor

p0: Point = Point (1.0, 2.0)
p0.scale_by(2.0)

