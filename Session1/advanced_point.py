from color_point import ColorPoint

class AdvancedPoint(ColorPoint):  # Inheriting from ColorPoint
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
        if new_hue not in AdvancedPoint.PALETTE:
            raise ValueError(f"hue must be one of: {AdvancedPoint.PALETTE}")
        self._hue = new_hue

    @property
    def color(self):
        # Provide compatibility with ColorPoint, using hue as color
        return self._hue

    @color.setter
    def color(self, new_color):
        if new_color not in AdvancedPoint.PALETTE:
            raise ValueError(f"color must be one of: {AdvancedPoint.PALETTE}")
        self._hue = new_color

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
        return AdvancedPoint(x, y, hue)

# Example usage:
AdvancedPoint.extend_palette("amber")
pt2 = AdvancedPoint(1, 2, "amber")
pt2.hue = "blue"
pt3 = AdvancedPoint(-1, -2, "blue")
print(AdvancedPoint.euclidean_distance(pt2, pt3))
pt4 = AdvancedPoint.from_dict({"x": 44})
print(pt4)
