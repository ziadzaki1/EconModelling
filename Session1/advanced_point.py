from color_point import ColorPoint

class UniqueAdvancedPoint(ColorPoint):  # Inheriting from ColorPoint
    PALETTE = ["red", "green", "blue", "black", "white"]

    def __init__(self, x, y, hue):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be numeric")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be numeric")
        if hue not in self.PALETTE:
            raise ValueError(f"hue must be one of: {self.PALETTE}")
        self._x = x
        self._y = y
        self._hue = hue

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def hue(self):
        return self._hue

    @hue.setter
    def hue(self, new_hue):
        if new_hue not in UniqueAdvancedPoint.PALETTE:
            raise ValueError(f"hue must be one of: {UniqueAdvancedPoint.PALETTE}")
        self._hue = new_hue

    @classmethod
    def extend_palette(cls, new_hue):
        cls.PALETTE.append(new_hue)

    @staticmethod
    def euclidean_distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    @staticmethod
    def from_dict(info):
        x = info.get("x", 10)
        y = info.get("y", 20)
        hue = info.get("hue", "black")
        return UniqueAdvancedPoint(x, y, hue)

# Example usage:
UniqueAdvancedPoint.extend_palette("amber")
pt2 = UniqueAdvancedPoint(1, 2, "amber")
pt2.hue = "blue"
pt3 = UniqueAdvancedPoint(-1, -2, "blue")
print(UniqueAdvancedPoint.euclidean_distance(pt2, pt3))
pt4 = UniqueAdvancedPoint.from_dict({"x": 44})
print(pt4)
