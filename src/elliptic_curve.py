from src.point import Point
from gmpy2 import invert


class EllipticCurve:

    def __init__(self, size, p, a, b, gx, gy, order):
        self.size = size
        self.p = p
        self.a = a
        self.b = b
        self.generator = Point(gx, gy, self)
        self.order = order

    def calculate_differentiation(self, p1, p2):
        if p1 == p2:
            return ((3 * (p1.x * p1.x) + self.a) * invert(2 * p1.y, self.p)) % self.p
        else:
            return (((p1.y - p2.y) % self.p) * (invert(p1.x - p2.x, self.p))) % self.p

    def multiply_point_by_scalar(self, k, p):
        assert isinstance(k, int) and isinstance(p, Point) and k != 0
        binary_k = str(bin(k))[2:][::-1]
        q = None
        for i in range(0, len(binary_k)):
            if binary_k[i] == '1':
                q = p + q
            p = self.double_point(p)

        return q

    def add_points(self, p1, p2):
        assert isinstance(p1, Point) and isinstance(p2, Point)

        slope = self.calculate_differentiation(p1, p2)
        x = (slope * slope - p1.x - p2.x) % self.p
        y = (slope * (p1.x - x) - p1.y) % self.p
        return Point(x, y, self)

    def double_point(self, p):
        slope = self.calculate_differentiation(p, p)
        x = (slope * slope - 2 * p.x) % self.p
        y = (slope * (p.x - x) - p.y) % self.p
        return Point(x, y, self)

    def subtract_point(self, p1, p2):
        pass

    def is_on_curve(self, p):
        # None represent the identity
        return (p is None) or (((p.y ** 2) - (p.x ** 3) - self.a * p.x - self.b) % self.p == 0)
