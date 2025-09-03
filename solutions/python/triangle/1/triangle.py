def equilateral(sides):
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1] and 0 not in sides
    return is_triangle and sides.count(sides[0]) == 3


def isosceles(sides):
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1] and 0 not in sides
    return is_triangle and (sides.count(sides[0]) > 1 or sides.count(sides[1]) > 1)


def scalene(sides):
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1] and 0 not in sides
    return is_triangle and sides.count(sides[0]) == 1 and sides.count(sides[1]) == 1
