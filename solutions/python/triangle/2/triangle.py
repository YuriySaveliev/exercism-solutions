def equilateral(sides):
    return is_triangle(sides) and sides.count(sides[0]) == 3


def isosceles(sides):
    return is_triangle(sides) and (sides.count(sides[0]) > 1 or sides.count(sides[1]) > 1)


def scalene(sides):
    return is_triangle(sides) and sides.count(sides[0]) == 1 and sides.count(sides[1]) == 1


def is_triangle(sides):
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1] and 0 not in sides
