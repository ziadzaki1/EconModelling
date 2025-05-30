from point import Point  # File: point.py, Class: Point
import random

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Initializes a FancyPoint with x, y, and shade
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"({self.x}|{self.y})[{self.color}]"

if __name__ == '__main__':  # Ensures this code runs only when executed directly
    color_points = []
    shades = ["crimson", "azure", "lime", "gold", "charcoal", "ivory", "violet"]
    for _ in range(5):
        pt = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(shades)
        )
        color_points.append(pt)
    print("Random fancy points:")
    print(color_points)
    color_points.sort()
    print("Fancy points sorted by distance from origin:")
    print(color_points)
