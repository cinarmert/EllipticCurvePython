class Point:

    def __init__(self, x, y, curve):
        self.x = int(x)
        self.y = int(y)
        self.curve = curve

    def __add__(self, other):
        # treat other point as identity
        if other is None:
            return self
        return self.curve.add_points(self, other)

    def __radd__(self, other):
        # treat other point as identity
        if other is None:
            return self
        return self.curve.add_points(self, other)

    def __mul__(self, scalar):
        if isinstance(scalar, int):
            return self.curve.multiply_point_by_scalar(scalar, self)
        raise ValueError("Expected scalar value")

    def __rmul__(self, scalar):
        if isinstance(scalar, int):
            return self.curve.multiply_point_by_scalar(scalar, self)
        raise ValueError("Expected scalar value")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
