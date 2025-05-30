from point import Point  # File: point.py, Class: Point
import random

class FancyPoint(Point):
    def __init__(self, x, y, shade):
        """
        Initializes a FancyPoint with x, y, and shade
        """
        self.x = x
        self.y = y
        self.shade = shade

    def __str__(self):
        return f"({self.x}|{self.y})[{self.shade}]"

if __name__ == '__main__':  # Ensures this code runs only when executed directly
    fancy_points = []
    shades = ["crimson", "azure", "lime", "gold", "charcoal", "ivory", "violet"]
    for _ in range(5):
        pt = FancyPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(shades)
        )
        fancy_points.append(pt)
    print("Random fancy points:")
    print(fancy_points)
    fancy_points.sort()
    print("Fancy points sorted by distance from origin:")
    print(fancy_points)
