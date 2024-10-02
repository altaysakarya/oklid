import math
import random

class Coordinate:
    def __init__(self, x, y):
        assert isinstance(x, int), "x must be an integer"
        assert isinstance(y, int), "y must be an integer"

        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        return 'Coordinate(%s, %s)' % (self.x, self.y)

points = [Coordinate(random.randint(1, 10), random.randint(1, 10)) for i in range(10)]

def calculate_distance(coordinate_1: Coordinate, coordinate_2: Coordinate):
    process_one = (coordinate_2.x - coordinate_1.x) ** 2
    process_two = (coordinate_2.y - coordinate_1.y) ** 2
    return (process_one + process_two) ** .5

def get_minimum(iterable):
    assert isinstance(iterable, list), "iterable must be a list"
    assert all(isinstance(item, float) for item in iterable), "All elements in iterable must be integers"

    i = float('inf')
    for j in iterable:
        if j < i:
            i = j
    return i

points = [Coordinate(random.randint(1, 10), random.randint(1, 10)) for i in range(10)]

distances = []

for i in range(0, len(points), 2):
    pair = points[i:i+2]
    if len(pair) == 2:
        point1, point2 = pair
        result = calculate_distance(point1, point2)
        distances.append(result)

minimum = get_minimum(distances)
text = "The shortest distance between points is %s" % minimum
print(text)