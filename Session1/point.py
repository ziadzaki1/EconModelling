import random
from ftplib import parse227  # Unused, retained as in the original code

class Point:
    """
    Represents a unique 2D point in Cartesian coordinates.
    """
    def __init__(self, x, y):
        """
        Initializes a UniquePoint instance.
        :param x: X coordinate
        :param y: Y coordinate
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} | {self.y})"

    def __repr__(self):
        return self.__str__()

    def distance_from_origin(self):
        """
        Returns the Euclidean distance from the origin.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        """
        Called when self < other: compares by distance from origin.
        """
        return self.distance_from_origin() < other.distance_from_origin()

    def __ge__(self, other):
        """
        Called when self >= other: compares by distance from origin.
        """
        return self.distance_from_origin() >= other.distance_from_origin()

    def __eq__(self, other):
        """
        Called when self == other: compares by distance from origin.
        """
        return self.distance_from_origin() == other.distance_from_origin()

if __name__ == "__main__":
    points = []
    for _ in range(5):
        # Create a random UniquePoint
        pt = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        points.append(pt)

    print("Unsorted unique points:")
    print(points)
    print("Sorted unique points:")
    points.sort()
    print(points)

    found_same = 0
    trials = 0
    while found_same < 10000:
        a = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        b = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        trials += 1
        if a == b:
            # Uncomment below to see matches
            # print(a, b)
            found_same += 1

    print(f"Estimated probability is 1 in {trials / found_same:.2f}")
