def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) != 3 


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides):
    return all(sum(sides) >= 2 * side for side in sides) and 0 not in sides
